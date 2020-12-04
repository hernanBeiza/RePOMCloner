import os
from sys import argv

def main(argv=None):
  print("brancher")
  if(argv==None):
    carpeta = input("Ingresa la carpeta contenedora de tus repositorios: ");
    rama = input("Ingresa la rama a la que quieres cambiarte: ");
  else:
    main,carpeta,rama = argv;
  leer(carpeta,rama);

def leer(carpeta,rama):
  print("leer " +carpeta);
  if(carpeta.endswith("/")==False):
    carpeta+="/"
  carpetas = os.listdir(carpeta);
  for item in carpetas:
    ruta = carpeta+item
    if(os.path.isdir(ruta)):
      print(item)
      linea = "cd " + ruta +" && git checkout " + rama +" && git pull"
      os.system(linea)

if __name__ == '__main__':
  if len(argv) < 2:
    print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar carpeta contenedora y rama");
  else:
    main(argv)