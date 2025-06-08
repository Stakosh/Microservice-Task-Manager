# Iniciamos nuestr imagen con la de python 3.13 ligera
FROM python:3.13.3-slim

# Definimos el directorio que servirá como el directorio principal de la app.
WORKDIR /app

# Copiamos nuestro código en la imagen.
COPY main.py /app/
#COPY tasks.json /app/

# Comando para ejecutar el código.
CMD ["python", "main.py"]

