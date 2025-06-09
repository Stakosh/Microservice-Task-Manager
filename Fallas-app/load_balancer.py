from flask import Flask, request, Response
import requests
import random
import time
import threading
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("balancer.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("balanceador")

app = Flask(__name__)

# Lista de servidores backend
SERVERS = [
    "http://localhost:5001",
    "http://localhost:5002"
]

# Registrar servidores caídos y su tiempo de caída
failed_servers = {}
RETRY_INTERVAL = 30  # Tiempo en segundos para reintentar con un servidor caído
HEALTH_CHECK_INTERVAL = 5  # Segundos entre health checks


def check_server_health(server):
    """Verificar si un servidor está activo"""
    try:
        response = requests.get(f"{server}/health", timeout=2)
        return response.status_code == 200
    except Exception as e:
        logger.warning(f"Error en health check para {server}: {str(e)}")
        return False


def get_active_servers():
    """Retorna lista de servidores activos basado en el estado actual"""
    current_time = time.time()
    active_servers = []

    for server in SERVERS:
        # Si el servidor no está en la lista de fallidos, o ha pasado el tiempo de reintento
        if server not in failed_servers or current_time - failed_servers[server] > RETRY_INTERVAL:
            active_servers.append(server)

    # Si hay servidores activos, retornar lista ordenada aleatoriamente
    if active_servers:
        random.shuffle(active_servers)
        return active_servers

    # Si no hay servidores activos, intentar con todos como último recurso
    logger.error("¡ALERTA! No hay servidores activos disponibles. Intentando con todos.")
    random.shuffle(SERVERS)
    return SERVERS


def health_check_loop():
    """Función que verifica periódicamente el estado de los servidores"""
    while True:
        for server in SERVERS:
            is_healthy = check_server_health(server)

            if is_healthy and server in failed_servers:
                # Servidor recuperado
                del failed_servers[server]
                logger.info(f"⚡ Health check: Servidor {server} recuperado y vuelve a estar activo")
            elif not is_healthy and server not in failed_servers:
                # Servidor caído
                failed_servers[server] = time.time()
                logger.warning(f"❌ Health check: Servidor {server} detectado como caído")

        # Esperar hasta el próximo health check
        time.sleep(HEALTH_CHECK_INTERVAL)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Obtener servidores activos
    active_servers = get_active_servers()

    # Intentar con cada servidor hasta encontrar uno que funcione
    last_error = None

    for server in active_servers:
        url = f"{server}/{path}"

        # Crear una nueva solicitud al servidor seleccionado
        method = request.method
        headers = {k: v for k, v in request.headers if k != 'Host'}
        data = request.get_data()

        try:
            # Reenviar la solicitud al servidor seleccionado
            resp = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                cookies=request.cookies,
                params=request.args,
                allow_redirects=False,
                stream=True,
                timeout=3  # Tiempo de espera para detectar rápidamente servidores caídos
            )

            # Si llegamos aquí, la solicitud fue exitosa
            logger.info(f"✅ Solicitud exitosa a: {url}")

            # Si el servidor estaba marcado como caído, quitarlo de la lista
            if server in failed_servers:
                del failed_servers[server]
                logger.info(f"⚡ Servidor {server} recuperado y vuelve a estar activo")

            # Crear una respuesta Flask a partir de la respuesta del servidor
            response = Response(
                resp.content,
                resp.status_code,
                [
                    (k, v) for k, v in resp.headers.items()
                    if k.lower() not in ('transfer-encoding', 'content-encoding', 'content-length')
                ]
            )

            # Agregar un encabezado personalizado que indica qué servidor atendió la solicitud
            response.headers['X-Upstream-Server'] = server

            return response

        except Exception as e:
            # Registrar el error pero sin mostrar detalles técnicos
            last_error = e
            logger.error(f"❌ Error al conectar con {server}: {str(e)}")
            failed_servers[server] = time.time()
            # Continuar con el siguiente servidor

    # Si llegamos aquí, todos los servidores intentados fallaron
    error_response = f"No se pudo completar la solicitud. Todos los servidores están caídos o no responden."
    logger.critical(f"TODOS LOS SERVIDORES FALLARON. Último error: {str(last_error)}")
    return error_response, 503


@app.route('/status', methods=['GET'])
def server_status():
    """Endpoint para verificar el estado de los servidores"""
    status = {}

    for server in SERVERS:
        if server in failed_servers:
            downtime = time.time() - failed_servers[server]
            status[server] = {
                "status": "DOWN",
                "downtime_seconds": int(downtime),
                "retry_in": max(0, int(RETRY_INTERVAL - downtime))
            }
        else:
            status[server] = {"status": "UP"}

    active_count = sum(1 for server in SERVERS if server not in failed_servers)

    html = f"""
    <html>
    <head>
        <title>Estado del Balanceador</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            .server {{ margin-bottom: 10px; padding: 10px; border-radius: 5px; }}
            .up {{ background-color: #d4edda; color: #155724; }}
            .down {{ background-color: #f8d7da; color: #721c24; }}
            .summary {{ margin-top: 20px; font-weight: bold; }}
        </style>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>Estado de los Servidores</h1>
    """

    for server, info in status.items():
        if info["status"] == "UP":
            html += f'<div class="server up">✅ {server}: ACTIVO</div>'
        else:
            html += f'<div class="server down">❌ {server}: CAÍDO (por {info["downtime_seconds"]} segundos, reintento en {info["retry_in"]} segundos)</div>'

    html += f'<div class="summary">Servidores activos: {active_count} de {len(SERVERS)}</div>'
    html += """
    </body>
    </html>
    """

    return html


# Verificar que los servidores estén activos al inicio
def check_servers_on_startup():
    logger.info("Verificando servidores al inicio...")
    for server in SERVERS:
        if check_server_health(server):
            logger.info(f"✅ Servidor {server} activo")
        else:
            failed_servers[server] = time.time()
            logger.warning(f"❌ Servidor {server} no responde al inicio")


if __name__ == '__main__':
    # Verificar servidores al inicio
    check_servers_on_startup()

    # Iniciar el thread de health check
    health_thread = threading.Thread(target=health_check_loop, daemon=True)
    health_thread.start()

    logger.info("Balanceador de carga iniciado en http://localhost:8080")
    logger.info("Puedes verificar el estado de los servidores en http://localhost:8080/status")
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)