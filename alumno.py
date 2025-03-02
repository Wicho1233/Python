
#Definir clase 
class alumno :
    #Definir parametros teniendo self como base
    def __init__(self,nombre,edad,carrera,nota):
        self.nombre = nombre
        self.edad =edad
        self.carrera=carrera
        self.nota=nota
  #Funciones en la clase
    def aprobado(self):
      if self.nota >=5 :
         return 'Aprobado'
      else:
         return  'No aprobo' 
        







