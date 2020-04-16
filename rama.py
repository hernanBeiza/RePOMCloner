import os
from sys import argv

def main(argv):
  print("main: rama")
  print(argv)
  main,carpeta,rama = argv
  leer(carpeta,rama)

def leer(carpeta,rama):
  print("leer")  
  carpetas = os.listdir(carpeta);
  for item in carpetas:
    ruta = carpeta+item
    if(os.path.isdir(ruta)):
      print(item)
      linea = "cd " + ruta +" && git checkout " + rama
      os.system(linea)

if __name__ == '__main__':
  if len(argv) < 2:
    print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar archivo , repositorio y archivo pom.xml");
  else:
    main(argv)