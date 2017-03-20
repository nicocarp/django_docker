# django_docker

Tp final para Adminmistracion de Redes y Seguridad: django + nginx + postgres en contenedores Docker

Para iniciar la aplicacion, descargar el repo y ejecutar los siguientes comandos con docker instalado.

docker-compose build
docker-compose run web python manage.py migrate
docker-compose up
-- Luego en otra terminal
docker ps
-- copiar id del contenedor ejecutandose correspondiente al contenedor web.
docker exec -ti <id_contenedor_web> python manage.py createsuperuser

Por ultimo ir al navegador y entrar en localhost:8080

Luego de la primera vez, solo ejecutar 
docker-compose up -d
