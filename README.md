# RePOMCloner

Conjunto de scripts en Python útiles para proyectos de múltiples repositorios, como microservicios SpringBoot.

### CLIs

- brancher: Cambiar todos los repositorios a una rama específica
- cleaner: Ejecutar mvn clean install en todos los repositorios de una carpeta
- puller: Ejecutar git pull en todos los repositorios de una carpet
- repomcloner: Clona uno a uno todos los módulos de un archivo pom.xml

## Ejecución

Revisar archivo README.md de cada CLI

```
python repomcloner.py repobase pom.xml
```

## Dependencias

- python
- os
- dom

## Futuro

- Crear una gran CLI para englobar todos estos CLI
