# Arquitectura de Sistemas: TICS317 – Microservice Task Manager

![Logo UAI](../mvc/assets/UAI.png)

---

## 📚 Descripción del Proyecto

**Microservice Task Manager** es un caso de estudio para la asignatura **Arquitectura de Sistemas (TICS317)**. Consiste en una aplicación basada en arquitectura de microservicios que permite gestionar tareas (crear, listar, completar y eliminar) a través de servicios independientes que se comunican mediante HTTP.

Cada microservicio es responsabilidad de una capa específica:

- **Client**: Interfaz web Flask para crear y visualizar tareas y logs.
- **Task Service**: Lógica de negocio de CRUD de tareas.
- **Storage Service**: Persistencia en archivo JSON (`tasks.json`).
- **Logging Service**: Registro de eventos en `log.txt`.
- **Notification Service** (WIP): Punto de partida para notificaciones.

---

## 🌿 Tecnologías y Dependencias

| Categoría            | Biblioteca                                      | Descripción                                            |
|----------------------|-------------------------------------------------|--------------------------------------------------------|
| **Lenguaje**         | Python 3.7+                                     | Versión recomendada: 3.7 o superior                    |
| **Framework Web**    | Flask                                           | Microframework para APIs y frontend ligero             |
| **HTTP Client**      | requests                                        | Comunicación REST entre microservicios                 |

Instálalas con:
```bash
pip install -r requirements.txt
```

---

## 🏷️ Estructura del Repositorio y Ramas

```bash
├── LICENSE
├── README.md
├── requirements.txt
├── client/
│   ├── app.py
│   └── templates/index.html
└── services/
    ├── logging_service/
    ├── notification_service/
    ├── storage_service/
    └── task_service/
```

**Ramas disponibles para revisión:**
- `javi1` – Implementación del proyecto por el estudiante **Javi Soto**.
- `javi2` – Implementación del proyecto por el estudiante **[Nombre Estudiante 2]**.

> Cambia de rama para revisar cada propuesta:
> ```bash
> git checkout javi1   # Revisión de la versión de Javi Soto
> git checkout javi2   # Revisión de la versión del otro estudiante
> ```

---

## 🚀 Ejecución de los Servicios

Arranca cada servicio en terminales separadas en este orden:

1. **Storage Service** (Puerto 5002):
   ```bash
   cd services/storage_service
   python app.py
   ```
2. **Logging Service** (Puerto 5003):
   ```bash
   cd services/logging_service
   python app.py
   ```
3. **Notification Service** (Puerto 5004):
   ```bash
   cd services/notification_service
   python app.py
   ```
4. **Task Service** (Puerto 5001):
   ```bash
   cd services/task_service
   python app.py
   ```
5. **Cliente Web** (Puerto 5000):
   ```bash
   cd client
   python app.py
   ```

> Asegúrate de respetar el orden para que las dependencias estén disponibles.

---

## 🔗 Endpoints Principales

| Servicio            | Método   | Ruta                          | Descripción                             |
|---------------------|----------|-------------------------------|-----------------------------------------|
| **Client**          | GET      | `/`                           | Interfaz web (lista tareas y logs)      |
|                     | POST     | `/add`                        | Agregar nueva tarea                     |
|                     | GET      | `/complete/<id>`              | Marcar como completada                  |
|                     | GET      | `/delete/<id>`                | Eliminar tarea                          |
| **Task Service**    | GET      | `/tasks`                      | Listar tareas                           |
|                     | POST     | `/tasks`                      | Crear tarea                             |
|                     | PUT      | `/tasks/<id>/complete`        | Completar tarea                         |
|                     | DELETE   | `/tasks/<id>`                 | Eliminar tarea                          |
| **Storage Service** | GET      | `/storage/tasks`              | Obtener tareas                          |
|                     | POST     | `/storage/tasks`              | Guardar lista de tareas                 |
| **Logging Service** | GET      | `/logs`                       | Obtener logs                            |
|                     | POST     | `/log`                        | Registrar evento                        |
| **Notification**    | GET      | `/status`                     | Estado del servicio (WIP)               |
|                     | POST     | `/notify`                     | Recibir notificación (WIP)              |

---

