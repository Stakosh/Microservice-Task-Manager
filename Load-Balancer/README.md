Load Balancer

Este proyecto incluye dos componentes:

1. Una aplicación Flask para la gestión de tareas.
2. Un balanceador de carga que distribuye peticiones entre varias instancias de TaskFlow.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.7+.
- Docker (opcional, si prefieres ejecutar con contenedores).
- Las dependencias de Python:
  ```bash
  pip install -r requirements.txt
  ```

---

## 1. Ejecución (app.py)

1. En una terminal, sitúate en la carpeta raíz del proyecto:
   ```bash
   cd ruta/al/proyecto
   ```
2. Arranca una instancia de Flask indicando el puerto (por defecto 5000):
   ```bash
   python app.py 5001
   ```
  Para alta disponibilidad, inicia varias instancias cambiando el puerto (p. ej. 5002, 5003, hasta 5004 en mi caso):
   ```bash
   python app.py 5002
   ```
   ```bash
   python app.py 5003
   ```
   ```bash
   python app.py 5004
   ```
3. Accede a:
   - **Interfaz web**: http://localhost:<PUERTO>
   - **API REST**: http://localhost:<PUERTO>/api
– Para acceder a cada servidor por separado, sustituyes <PUERTO> por 5001, 5002 o 5003 según te interese:


---

## 2. Ejecución del Load Balancer (load_balancer.py)

1. Tras iniciar al menos dos instancias de app.py, en otra terminal ejecuta:
   ```bash
   python load_balancer.py
   ```
2. El balanceador expondrá:
   - **App**: http://localhost:8080  (redirige circularmente a los servidores disponibles)
   - **Dashboard**: http://localhost:8080/lb-status
   - **API de estadísticas**: http://localhost:8080/lb-api/stats

---

## 3. Ejemplos de uso via API

- **Agregar una tarea**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"title": "nueva tarea"}' \
       http://localhost:8080/api/tasks
  ```

- **Consultar tareas**:
  ```bash
  curl http://localhost:8080/api/tasks
  ```

---

## 4. Cómo ejecutar `main.py` y probar el Load Balancer

Estos pasos asumen que tienes dos scripts en la raíz: `app.py` y `main.py` (equivalente a `load_balancer.py`).

1. **Instalar dependencias**:
   ```bash
   pip install flask requests
   ```

2. **Abrir tres terminales**:
   - **Terminal A** – Primer servidor
   - **Terminal B** – Segundo servidor
   - **Terminal C** – Balanceador de carga

3. **Iniciar el primer servidor (puerto 5001)**
   ```bash
   cd C:/Users/JaviS/Documents/tics317/balanceador
   python app.py 5001
   ```
   Deberías ver:
   ```
    * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
   ```

4. **Iniciar el segundo servidor (puerto 5002)**
   ```bash
   cd C:/Users/JaviS/Documents/tics317/balanceador
   python app.py 5002
   ```
   Y:
   ```
    * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
   ```

5. **Iniciar el balanceador (main.py)**
   ```bash
   cd C:/Users/JaviS/Documents/tics317/balanceador
   python main.py
   ```
   Por defecto escuchará en http://127.0.0.1:8080/ y mostrará:
   ```
    * Load Balancer running on http://127.0.0.1:8080/
   ```

6. **Probar la aplicación**:
   - http://localhost:8080  → vía balanceador
   - http://localhost:5001  → servidor 1
   - http://localhost:5002  → servidor 2

   Agrega/elimina tareas y observa cómo se reparte la carga (cambio de color, round-robin entre puertos).

> **Tip:** Para opciones adicionales en `main.py`, ejecuta:
> ```bash
> python main.py --help
> ```

---

## 5. Persistencia de datos con Docker

Si ejecutas la aplicación en Docker, `tasks.json` se crea dentro del contenedor y desaparece al detenerlo. Para persistir:

```bash
docker run -it -v "${PWD}:/app" task-manager
```

Así, `tasks.json` se guardará en tu carpeta local.

---

## 6. Compartir la imagen Docker

1. **Guardar la imagen en un archivo**:
   ```bash
   docker save -o task-manager.tar task-manager
   ```
2. **Cargar la imagen en otro equipo**:
   ```bash
   docker load -i task-manager.tar
   ```
3. **Ejecutar**:
   ```bash
   docker run -it task-manager
   ```
