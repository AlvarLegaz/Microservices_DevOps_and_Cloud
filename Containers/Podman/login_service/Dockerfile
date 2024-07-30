# Usar una imagen base de Python
FROM python:3.9-alpine

# Establecer un directorio de trabajo
WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers

# Copiar los requerimientos del proyecto
COPY ./requirements.txt .

# Instalar los requerimientos del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY ./app ./app

ENV PYTHONPATH=.

# Establecer la variable de entorno FLASK_APP
ENV FLASK_APP=./app/services/login/api_login.py

# Exponer el puerto en el que se ejecutará Flask
EXPOSE 3000

# Comando para iniciar el servidor Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
