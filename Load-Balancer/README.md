
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
– Para acceder a cada servidor por separado, sustituyes <PUERTO> por 5001, 5002 o 5003 según te interese


---

## 2. Ejecución del Load Balancer (load_balancer.py)

1. Tras iniciar al menos dos instancias de app.py, en otra terminal ejecuta:
   ```bash
   python load_balancer.py
   ```
2. El balanceador expondrá:
   - **App**: http://localhost:8080  (redirige circularmente a los servidores disponibles)


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


Persistencia de datos con Docker

Si ejecutas la aplicación en Docker, `tasks.json` se crea dentro del contenedor y desaparece al detenerlo. Para persistir:

```bash
docker run -it -v "${PWD}:/app" task-manager
```

Así, `tasks.json` se guardará en tu carpeta local.

---

 Compartir la imagen Docker

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
