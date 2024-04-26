FROM python:3.8

# Copia los archivos de la aplicación al contenedor
COPY . .

# Establece el directorio de trabajo en /opt/app
WORKDIR /opt/app

# Instala Poetry y las dependencias del proyecto
RUN pip install poetry && poetry install
