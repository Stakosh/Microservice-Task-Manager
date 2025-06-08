# Microservice Task Manager

Este proyecto implementa un sistema de gestión de tareas basado en una arquitectura de **microservicios**. Permite crear, listar, completar y eliminar tareas a través de una interfaz web.

## 🚀 Tecnologías utilizadas
- Python 3.13+
- Flask
- HTML/CSS (Bootstrap-like)
- JSON para almacenamiento ligero

---

## 🌐 Arquitectura y servicios

Cada servicio corre en un puerto diferente, facilitando su desarrollo, despliegue y escalabilidad.

| Servicio               | Puerto | Descripción                                                                |
|------------------------|--------|-----------------------------------------------------------------------------|
| `client`               | 5000   | Interfaz web para el usuario. Redirige peticiones a `task_service`.        |
| `task_service`         | 5001   | Gestiona lógicamente las tareas (crear, completar, eliminar).              |
| `storage_service`      | 5002   | Encargado de guardar y leer las tareas en un archivo `tasks.json`.         |
| `logging_service`      | 5003   | Registra eventos y errores en `log.txt`.                                   |
| `notification_service` | 5004   | Muestra notificaciones por consola. Puede omitirse.                         |

---

## 📂 Estructura del proyecto

```
microservice-task-manager/
│
├── client/
│   ├── templates/
│   │   └── index.html         # Interfaz del usuario
│   ├── app.py                 # Frontend Flask que consume la API
│   └── __init__.py
│
├── task_service/
│   ├── app.py                 # Expone lógica de tareas (GET, POST, PUT, DELETE)
│   └── __init__.py
│
├── storage_service/
│   ├── app.py                 # Accede y modifica tasks.json
│   ├── tasks.json             # Archivo persistente con las tareas
│   └── __init__.py
│
├── logging_service/
│   ├── app.py                 # Registra logs
│   ├── log.txt                # Archivo de logs (creado automáticamente)
│   └── __init__.py
│
├── notification_service/
│   ├── app.py                 # Muestra mensajes en consola (opcional)
│   └── __init__.py
│
├── run_all.bat               # Script para levantar todos los servicios
├── requirements.txt          # Dependencias del sistema
└── README.md                 # Este documento
```

---

## ✍️ Instalación y ejecución

### 📆 1. Clona este repositorio
```bash
git clone https://github.com/usuario/microservice-task-manager.git
cd microservice-task-manager
```

### 🌟 2. Crea y activa un entorno virtual (recomendado)
```bash
python -m venv env
env\Scripts\activate  # En Windows
# o
source env/bin/activate  # En Linux/Mac
```

### ⭐ 3. Instala dependencias
```bash
pip install -r requirements.txt
```

### 💡 4. Ejecuta todos los servicios
```bash
./run_all.bat
```

Este script abrirá 4 o 5 terminales, una por servicio. Cada microservicio corre de forma independiente.

---

## 🔄 Interacción entre servicios

- `client` (5000) renderiza la interfaz y llama a las rutas del `task_service`.
- `task_service` (5001) se comunica con:
  - `storage_service` (5002) para guardar y recuperar tareas.
  - `logging_service` (5003) para dejar registro de acciones.
  - `notification_service` (5004) para mostrar notificaciones (opcional).

---

## ⚠️ Notas importantes
- **No modifiques directamente `tasks.json`** salvo que entiendas el formato.
- Puedes detener todos los servicios cerrando sus terminales o con `CTRL+C`.

---

## 📄 Autor y licencia

Creado por Javiera Soto. Uso educativo y libre para proyectos personales.

---

❤️ Si te sirvió este proyecto, ¡no dudes en compartirlo o dejar una estrella!