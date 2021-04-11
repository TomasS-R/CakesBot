FROM python:3.7

RUN pip install --upgrade pip \
    #Crea una carpeta llamada app dentro del contenedor
    && mkdir /app

#Agregar archivos a la carpeta add
ADD . /app

#Establecemos el directorio de trabajo en la carpeta app
WORKDIR /app

#Instalamos el archivo de requerimientos
RUN pip install -r requeriments.txt

CMD python /app/CakesAndChocolats.py