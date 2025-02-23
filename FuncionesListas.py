nombres=['Juan','Pablo',"Laura"]
edades = [23,25,21,34,21,45]
edades2 = [34,56,32,56]
aprobado =[True,False,True]

#Funcion count la cantidad de veces que aparec un elemento en una lista
print(edades.count(21))

#Fucion extend para agregar elementos de otra lista
#edades.extend(edades2)
print(edades)

#Funcion pop elimina un elemento de una lista pero lo va adevolver
print(edades.pop(4),'\n',edades)

#Funcion reverse devuelve elementos de manera inversa
nombres.reverse()
print(nombres)

#Funcion sort va a ordnar la lista de manera alfabetica o numerica
edades.sort()
nombres.sort()
print(edades,'\n',nombres)

#Funcion copy permite copiar listas
edades_copia=edades.copy()

print(edades_copia)
print(edades)