#Las tuplas son inmutables durante todo el programa
alumnos=('Juan','Pedro','Laura')
edades=(23,25,21,21)
aprobado=(True,False,True)

print(alumnos,'\n',edades,'\n',aprobado)

print(edades[0])

edadJuan = edades[0]
edadJuan += 1
print(edades[0])

#len longitud de la Tupla
print(len(alumnos))

#index posicion en la que se encontraba un elemento
print(edades.index(23))

#Count cuantas veces se repite un elemento en la tupla
print(edades.count(21))