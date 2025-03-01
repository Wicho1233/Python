

#Declarar variable para guardar el archivo
#R permite leer el archivo
archivo = open("alumnos.txt","r")

#print(archivo.readable())


#print(archivo.read())


#print(archivo.readline())
#print(archivo.readline())

print(archivo.readlines()[0])

for alumno in archivo.readlines():
    print(alumno)

archivo.close()



