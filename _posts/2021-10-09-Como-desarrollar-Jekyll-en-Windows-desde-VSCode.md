---
title: Como desarrollar Jekyll en Windows desde VSCode
author: Ismael Delgado
date: 2021/10/09 19:02:38 +0000
categories: ['Otros']
tags: ['VSCode', 'Windows', 'Jekyll', 'Contenedores', 'Docker']
render_with_liquid: false
---

## Requisitos para empezar

### Docker Desktop
Lo primero que hay que hacer es instalar Docker Desktop (https://www.docker.com/products/docker-desktop), que se encargará de activar todos los requisitos necesarios, así como el WSL2. 

### Extensión "Remote - Containers" en VSCode

El siguiente paso es instalar la extensión "remote containers" de VSCode. Para ello, simplemente accedemos a la pestaña de extensiones de VSCode y lo instalamos mediante el buscador. 

## Ejecutando Jekyll en VSCode

Una vez realizados los pasos anteriores, abrimos en VSCode la carpeta en la que tenemos nuestro proyecto de Jekyll. Una vez dentro, accedemos a la paleta de comandos (F1 o Crtl+Shift+P) y ejecutamos la opción "Remote-Containers: Open Folder in Container". En este momento nos preguntará qué carpeta queremos abrir en el contenedor, por lo que selecionamos la carpeta del proyecto. 

A continuación, nos aparecerá una lista con las imágenes disponibles. Seleccionamos la opción "Show All Definitions" para verlas todas y después buscamos "Jekyll". A partir de este momento tendremos que escoger la versión deseada, que en mi caso ha sido "buster" con Node.js versión "16". 

Ahora solo hay que esperar a que se termine de configurar el contenedor. La primera vez tardará bastante tiempo, pero las siguientes veces será mucho más rápido. 

Una vez creado el contenedor, ya tendremos Jekyll funcionando en un contenedor conectado con VSCode. Para ejecutar nuestra página abrimos un nuevo terminal: 

Y lanzamos la página con "jekyll serve": 

Y ya podemos acceder desde el navegador a la página web (localhost:4000), en la que se reflejarán todos los cambios que hagamos desde VSCode en directo. 

