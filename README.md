<<<<<<< HEAD
# django_docker
=======
Administracion de Redes y Seguridad 2017
=========================================

### Django + Postgres + nginx + celery en contenedores Docker ###


  - [Contenido](#contenido)
  - [Requerimientos](#requerimientos)
  - [Iniciar la Aplicacion](#iniciar-la-aplicacion)
  - [Para probar Celery](#para-probar-celery)
  

## Contenido ##

``web/``
---------

Aplicacion Django Farma 2015. Modificamos settings para poner la aplicacion en produccion: usar postgres, configuracion de celery, allowed_hosts, debug y demas.

``celery/``
---------

Contiene solo un script con comandos que se ejecutaran al momento de lanzar el contenedor worker. Este contenedor se crea a partir del mismo Dockerfile que web. 

``nginx/``
---------

Contiene su correspondiente Dockerfile con imagen nginx, y archivo de configuracion default.conf. Esta configuracion permite a nginx recuperar los archivos estaticos y trabajar como proxy_pass hacia nuestra contenedor web. 

## Requerimientos ##

  - [Docker][docker-path].
  - [Docker-compose][docker-compose-path]

[docker-path]: https://www.docker.com/get-docker/
[docker-compose-path]: https://docs.docker.com/compose/

## Iniciar la aplicacion ##

    $sudo chown -R $USER:$USER
    $ docker-compose build
    $ docker-compose up -d
    $ docker exec -ti finalseguridad_web_1 bash

Una vez dentro del contenedor web creamos un superusuario para acceder a la aplicacion

    $ python web/django_app/manage.py createsuperuser  

## Para probar Celery ##

    $ docker exec -ti finalseguridad_worker_1 bash
    $ python manage.py shell
    $ >>> from organizaciones import tasks
    $ >>> res = tasks.add.delay(2,5)

Vemos el log del contenedor worker el cual muestra el resultado.
>>>>>>> ab2d3ff4cbb2340b6b30f0a607ced497e22d7b75
