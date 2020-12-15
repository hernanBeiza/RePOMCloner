import os
from sys import argv
from xml.dom import minidom
from colorama import Fore, Back, Style, init
init(autoreset=True)

def main(argv=None):
  print("repomcloner")
  if(argv==None):
    repo = input("Ingresa la url del repositorio: ");
    """
    if not repo:
      repo = "https://dev.azure.com/CAPJ/Unificado/_git/";
      if(repo.endswith("/")==False):
        repo+="/"
    """
    entradaPom = input("Ingresa el archivo pom.xml: ");
  else:
    main,repo,entradaPom = argv
  leerPom(repo,entradaPom)

def leerPom(repo,entradaPom):
  #print("leerPom " + entradaPom);  
  try:
    pomXML = minidom.parse(entradaPom)
    carpetaSalida = os.path.dirname(entradaPom);
    modules = pomXML.getElementsByTagName('module')
    #print(modules)
    for module in modules:
      #print(module.firstChild.data)
      linea = "cd " + carpetaSalida +" && git clone "+repo+module.firstChild.data;
      print(Fore.CYAN + linea);
      os.system(linea)

  except IOError:
    print ("Error: Archivo Pom "+entradaPom+ " no existe.")

def limpiarSalida(archivoSalida):
  #print("limpiarSalida "+archivoSalida)
  try:
    raw = open(archivoSalida, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
  except IOError:
    print ("Error: Archivo "+archivoSalida+ " no existe.")

if __name__ == '__main__':
  if len(argv) < 3:
    #print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print(Fore.RED + "Falta especificar repo y archivo pom.xml");
    #main(None);
  else:
    main(argv)