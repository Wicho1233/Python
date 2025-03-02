#Para crear objetos hay que importar la clase
#Seleccionanado el archivo alumno y de ella la clase alumno
from alumno import alumno

#Definir objeto con el cual se puede acceder a diferentes parametros
alumno1 =alumno('Juan',22,'Arquitectura',4.1)
alumno2=alumno('Laura',21,'Sistemas',9.9)

#Manera de utilizar los objetos
print(alumno1.aprobado())
print(alumno2.nota)



