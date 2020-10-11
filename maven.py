import os
from sys import argv

def main(argv):
  print("main: maven")
  print(argv)
  main,carpeta = argv
  leer(carpeta)

def leer(carpeta):
  print("leer")  
  carpetas = os.listdir(carpeta);
  for item in carpetas:
    ruta = carpeta+item
    if(os.path.isdir(ruta)):
      print(item)
      linea = "cd " + ruta +" && mvn clean install"
      os.system(linea)

if __name__ == '__main__':
  if len(argv) < 2:
    print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar carpeta");
  else:
    main(argv)
