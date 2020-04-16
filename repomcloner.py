import os
from sys import argv
from xml.dom import minidom

def main(argv):
  print("main: repomcloner")
  print(argv)
  main,repo,entradaPom = argv
  leerPom(repo,entradaPom)

def leerPom(repo,entradaPom):
  print("leerPom")  
  try:
    pomXML = minidom.parse(entradaPom)
    carpetaSalida = os.path.dirname(entradaPom);
    print (carpetaSalida);

    modules = pomXML.getElementsByTagName('module')
    #print(modules)
    for module in modules:
      #print(module.firstChild.data)
      linea = "cd " + carpetaSalida +" && git clone "+repo+module.firstChild.data;
      print(linea)
      os.system(linea)

  except IOError:
    print ("Error: Archivo Pom "+entradaPom+ " no existe.")

def limpiarSalida(archivoSalida):
  print("limpiarSalida "+archivoSalida)
  try:
    raw = open(archivoSalida, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
  except IOError:
    print ("Error: Archivo "+archivoSalida+ " no existe.")

if __name__ == '__main__':
  if len(argv) < 1:
    print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar archivo pom.xml");
  else:
    main(argv)