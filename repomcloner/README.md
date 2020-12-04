# RePOMCloner

Script en Python que lee los modulso del archivo pom.xml y los clona uno a uno. 
Este script está pensando especialmente para un proyecto que contiene los módulos maven en un archivo pom.xml, como en APIs Rest en SpringBoot.

La salida de los módulos clonados tienen como destino la carpeta contenedora del archivo pom.xml, el cuál se pasa por parámetro al ejecutar el script.

## Ejecución

Recordar pasar el archivo pom.xml

```
python repomcloner.py repobase pom.xml
```

## Dependencias

- python
- os
- dom