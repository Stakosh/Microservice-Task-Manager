# Microservice-Task-Manager

**Proyecto de Arquitectura de Sistemas – Microservicios para Gestión de Tareas**

Esta aplicación demuestra una arquitectura de microservicios para la gestión de tareas, separando responsabilidades en servicios independientes que se comunican a través de HTTP.

---

## 📂 Estructura de Directorios

```
Microservice-Task-Manager/
├── LICENSE
├── README.md        # Este archivo
├── requirements.txt # Dependencias del proyecto
├── client/          # Interfaz web (Flask)
│   ├── app.py
│   └── templates/
│       └── index.html
└── services/        # Servicios backend
    ├── task_service/        # Lógica de CRUD de tareas
    │   └── app.py
    ├── storage_service/     # Persistencia de tareas (JSON)
    │   ├── app.py
    │   └── tasks.json       # Archivo de datos
    ├── logging_service/     # Registro de eventos
    │   ├── app.py
    │   └── log.txt          # Archivo de logs
    └── notification_service/ # Servicio de notificaciones (WIP)
        └── app.py
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

---

## 📥 Instalación

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Microservice-Task-Manager
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Ejecución de los Servicios

Se recomienda abrir **5 terminales** diferentes y ejecutarlos en el siguiente orden:

1. **Storage Service** (Puerto 5002)
   ```bash
   cd services/storage_service
   python app.py
   ```
2. **Logging Service** (Puerto 5003)
   ```bash
   cd services/logging_service
   python app.py
   ```
3. **Notification Service** (Puerto 5004)
   ```bash
   cd services/notification_service
   python app.py
   ```
4. **Task Service** (Puerto 5001)
   ```bash
   cd services/task_service
   python app.py
   ```
5. **Cliente Web** (Puerto 5000)
   ```bash
   cd client
   python app.py
   ```

> **Tip:** Asegúrate de iniciar los servicios en este orden para que las dependencias de red (almacenamiento y logging) estén disponibles.

---

## 🔗 Arquitectura y Comunicación

- **Client (5000)**: Interfaz web en Flask. Consume los endpoints del Task Service y muestra tareas y logs.
- **Task Service (5001)**: Gestiona operaciones CRUD de tareas. Se comunica con:
  - **Storage Service** para persistencia (`/storage/tasks`).
  - **Logging Service** para registrar eventos (`/log`).
- **Storage Service (5002)**: Almacena y recupera la lista de tareas en un archivo `tasks.json`.
- **Logging Service (5003)**: Registra eventos en `log.txt` y los expone vía `/logs`.
- **Notification Service (5004)**: Servicio de notificaciones (en desarrollo), expone `/notify`.

---

## 📋 Endpoints Principales

### Client (5000)
- `GET /` — Vista principal (lista tareas y logs)
- `POST /add` — Agrega una nueva tarea
- `GET /complete/<id>` — Marca tarea como completada
- `GET /delete/<id>` — Elimina una tarea

### Task Service (5001)
- `GET /` — Health check
- `GET /tasks` — Listar tareas
- `POST /tasks` — Crear nueva tarea
- `PUT /tasks/<id>/complete` — Completar tarea
- `DELETE /tasks/<id>` — Eliminar tarea

### Storage Service (5002)
- `GET /storage/tasks` — Obtener todas las tareas
- `POST /storage/tasks` — Guardar lista de tareas

### Logging Service (5003)
- `GET /` — Health check
- `POST /log` — Registrar evento
- `GET /logs` — Obtener todos los logs

### Notification Service (5004)
- `GET /` — Health check
- `POST /notify` — Recibir notificación (WIP)
- `GET /status` — Estado del servicio (WIP)

---

## 💾 Persistencia

- **Tareas:** `services/storage_service/tasks.json`
- **Logs:** `services/logging_service/log.txt`

---

## 📝 Notas

- El servicio de notificaciones está en desarrollo y puede extenderse para enviar alertas reales.
- Los URLs y puertos están codificados en las variables de `app.py`. Se pueden externalizar mediante variables de entorno para mayor flexibilidad.
- Este proyecto sirve como referencia para diseñar y desplegar arquitecturas basadas en microservicios.

