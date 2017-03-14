AppDjango + nginx + postgres + gunicorn en contenedores Docker


Ejecutar los siguientes comandos para inicar la aplicacion:

1- sudo chown -R $USER:$USER .
2- docker-compose build  
3- docker-compose run web python app/manage.py migrate
4- docker-compose run web python app/manage.py createsuperuser
5- docker-compose up
6- ingresar 0.0.0.0:8080 en el navegador.

