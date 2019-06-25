
## Actividad de integracion con XML + DOM + Redis + Docker
**1.** Situarse dentro de la carpeta del proyecto y abrir una terminal

**2.** Crear la imagen de Docker que se usará para el cliente, desde el cual se ejecuta el programa:

`docker image build -t client_image .`

**3.** Crear una red, mediante la cual se comunicarán los containers involucrados:

`docker network create n1`

**4.** Correr un container a partir de la imagen oficial de Redis, el cual sera el servidor de la BD:

`docker run --name redis_sv --network n1 -d redis`

**5.** A su vez, se necesitará otro server de Redis para realizar los tests:

`docker run --name redis_sv_test --network n1 -p 6500:6379 -d redis`

**6.** Crear un container para el cliente a partir de la imagen construida antes. Éste tiene un bind mount referenciando a la carpeta del programa:

`docker container run -it --name cli --network n1 -v $(pwd)/program:/program client_image`

**7.** Dentro de la consola de “cli”:

`cd program`

y luego, para ejecutar el programa:

`python3 main.py`

<h4>Para correr los tests </h4>
- Con pytest, desde una nueva terminal, ubicado en `program`.


