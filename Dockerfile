FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install Django==1.8.17
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]	