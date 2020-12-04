import os
from sys import argv

def main(argv=None):
  print("main: puller")
  if(argv==None):
    carpeta = input("Ingresa la ruta de la carpeta contenedora de repositorios: ");
  else:
    main,carpeta = argv;
  leerCarpeta(carpeta);

def leerCarpeta(carpeta):
  print("leerCarpeta")
  if(carpeta.endswith("/")==False):
    carpeta+="/"
  carpetas = os.listdir(carpeta);
  for item in carpetas:
    ruta = carpeta+item
    if(os.path.isdir(ruta)):
      print(item)
      linea = "cd " + ruta +" && git pull"
      os.system(linea)

if __name__ == '__main__':
  if len(argv) < 2:
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar carpeta con repositorios");
  else:
    main(argv)