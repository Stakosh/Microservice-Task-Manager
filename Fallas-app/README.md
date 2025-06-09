## Arquitectura de Sistemas TICS317

Este repositorio contiene ejercicios de detección y monitoreo de errores HTTP en una aplicación Flask con un balanceador de carga.

### Requisitos

* Python 3.7+ instalado
* Entorno virtual (recomendado)
* IDE de tu preferencia (Visual Studio Code, PyCharm, etc.)

### Instalación

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\\Scripts\\activate.bat  # Windows
   ```
3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Estructura del proyecto

```
├── app.py             # Servidor Flask configurable por puerto
├── load_balancer.py   # Balanceador de carga en el puerto 8080
├── test_errors.py     # Pruebas de generación de errores HTTP
├── requirements.txt   # Librerías necesarias
└── README.md          # Instrucciones de uso
```

### Descripción del sistema

* **Cliente → Balanceador (8080) → Servidores Flask (5001, 5002) → Sistema de Logging.**
* Detecta errores HTTP: 400 (BAD\_REQUEST), 404 (NOT\_FOUND) y 500 (INTERNAL\_ERROR).
* Registra estadísticas y últimos 10 errores.

### Endpoints principales

* `GET /errors/stats`  : Devuelve estadísticas de errores.
* `GET /status`       : Estado del balanceador.
* `GET /health`       : Health check del balanceador.

### Ejecución

Abrir cuatro terminales y ejecutar:

1. **Servidor Flask 1 (puerto 5001)**

   ```bash
   python app.py 5001
   ```
2. **Servidor Flask 2 (puerto 5002)**

   ```bash
   python app.py 5002
   ```
3. **Balanceador de carga (puerto 8080)**

   ```bash
   python load_balancer.py
   ```
4. **Pruebas de errores**

   ```bash
   python test_errors.py
   ```

### Resultado esperado

```text
Total errores: 3
Tipos de errores: {'400_BAD_REQUEST': 1, '404_NOT_FOUND': 1, '500_INTERNAL_ERROR': 1}
```

---

¡Listo para sobrellevar la observabilidad y confiabilidad en tu arquitectura de sistemas!
