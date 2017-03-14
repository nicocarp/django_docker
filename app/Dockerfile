# Importante: la instruccion ADD <src> invalida la cache de todas las siguientes
# instrucciones si <src> se modifica. Ejemplo en el siguiente dockerfile, si se modifica
# el archivo requeriments.txt no invalida la cache para la instruccion install django.


FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install Django==1.8.17
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
	