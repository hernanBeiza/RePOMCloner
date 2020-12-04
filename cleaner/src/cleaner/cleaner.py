import os
from sys import argv

def main(argv=None):
  print("cleaner")
  if(argv==None):
    carpeta = input("Ingresa la carpeta contenedora de tus repositorios: ");
  else:
    main,carpeta = argv;
  leer(carpeta);

def leer(carpeta):
  print("leer " + carpeta);
  if(carpeta.endswith("/")==False):
    carpeta+="/"
  carpetas = os.listdir(carpeta);
  for item in carpetas:
    ruta = carpeta+item
    if(os.path.isdir(ruta)):
      print(item)
      linea = "cd " + ruta +" && mvn clean install"
      os.system(linea)

if __name__ == '__main__':
  if len(argv) < 2:
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar carpeta con repositorios");
  else:
    main(argv)