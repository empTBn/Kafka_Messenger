# Usa la imagen base de Python 3.11
FROM python:3.11

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

# Expone el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Comando para iniciar la aplicación Flask
CMD ["poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0"]
