#Para utilizar la herencia hay que exportar los archivos de los que se quiera obtener las clases
from animal import *

#Se coloca el nombre de la clase a heredar como parametros de la misma
#Asi se podran reutilizar las funciones de la clase seleccionada
class perro():
   def ladrar(self):
      print('El perro ladra')
   #La funcion toma diferentes formas pese a llamase igual que la que hereda   
   def comer(self):
      print('El perro come croquetas')  