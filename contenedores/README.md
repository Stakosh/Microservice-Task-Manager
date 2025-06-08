# Task Manager con Docker! 

## Definición de contenedor

Un contenedor es la instancia en ejecución de una imagen de software que incluye el código y todas sus dependencias, empaquetadas de forma estandarizada para garantizar un comportamiento rápido y fiable en cualquier entorno. A diferencia de las máquinas virtuales (VM), los contenedores comparten el kernel del sistema anfitrión, pero funcionan de manera aislada, ofreciendo mayor eficiencia, portabilidad y consistencia entre desarrollo, pruebas y producción.

## Comparativa: Máquina Virtual vs. Contenedor

| Característica          | Máquina Virtual (VM)                       | Contenedor                                   |
|-------------------------|--------------------------------------------|-----------------------------------------------|
| **Aislamiento**         | A nivel de sistema operativo completo      | A nivel de proceso                            |
| **Kernel**              | Cada VM ejecuta su propio kernel           | Comparten el kernel del anfitrión             |
| **Tamaño**              | Pesadas (incluyen SO completo)             | Ligeros (solo lo necesario para la app)       |
| **Arranque**            | Lento (inicia un SO completo)              | Rápido (ejecuta únicamente procesos)          |
| **Uso de recursos**     | Alto                                       | Bajo                                          |
| **Portabilidad**        | Dependen del hipervisor                    | Se ejecutan en cualquier sistema compatible   |
| **Casos de uso**        | Servidores virtuales, múltiples SO         | Microservicios, despliegue ágil de aplicaciones |

## ¿Por qué usar contenedores?

- **Autónomos:** Cada contenedor incluye todo lo necesario para ejecutarse sin dependencias externas.
- **Aislados:** Minimiza el impacto entre aplicaciones y en el sistema anfitrión, mejorando la seguridad.
- **Independientes:** Se gestionan por separado; eliminar uno no afecta al resto.
- **Portátiles:** El mismo contenedor funciona igual en desarrollo, centros de datos o nubes públicas.

## Ventajas de Docker

Docker facilita el empaquetado lógico de aplicaciones, abstraídas del entorno de ejecución. Esto permite implementaciones sencillas y coherentes, ya sea en un centro de datos privado, en la nube o en el equipo local de un desarrollador. Con Docker, puedes crear entornos predecibles y aislados que se ejecutan en cualquier lugar.

## Dockerfile

Un **Dockerfile** es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir una imagen. Permite automatizar el proceso de creación de imágenes usando comandos muy similares a los de Linux, sin necesidad de aprender una sintaxis nueva.

## Cómo ejecutar la aplicación en clase

1. **Construir la imagen** (en este ejemplo se llama `task-manager`):
   ```bash
   docker build -t task-manager .
   ```

2. **Ejecutar el contenedor**:
   ```bash
   docker run -it task-manager
   ```

> **Importante:** El código genera un archivo `tasks.json` dentro del contenedor, que desaparece al detenerlo. Para conservarlo localmente, monta un volumen:
>
> ```bash
> docker run -it -v "${PWD}:/app" task-manager
> ```
>
> Así, `tasks.json` se guardará en la carpeta donde se ejecute el comando.

## Compartir la imagen

1. **Guardar la imagen en un archivo TAR:**
   ```bash
   docker save -o task-manager.tar task-manager
   ```

2. **Importar la imagen en otro equipo:**
   ```bash
   docker load -i task-manager.tar
   ```

3. **Ejecutar en Docker Desktop:**
   ```bash
   docker run -it task-manager
   
