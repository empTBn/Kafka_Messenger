FROM python:3.8

# Variables de entorno para la base de datos MongoDB
ENV DB_HOST_MONGO=localhost
ENV DB_PORT_MONGO=27017
ENV DB_USER_MONGO=root
ENV DB_PASSWORD_MONGO=example

# Establece el directorio de trabajo en /opt/app
WORKDIR /opt/app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala Poetry y las dependencias del proyecto
RUN pip install poetry && poetry install
