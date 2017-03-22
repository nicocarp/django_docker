FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ENV NOMBRE_DB=postgres
ENV USUARIO_DB=postgres
ENV HOST_DB=db
ENV PORT_DB=5432

ADD . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]	