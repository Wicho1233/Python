#Listas pueden contener cualquier dato
nombres=['Juan','Pablo',"Laura"]
edades = [23,25,21]
aprobado =[True,False,True]


#Mostrar un dato por su posicion
print(nombres[0])

#Agregar elementos a una lista
nombres.append('Pedro')
edades.append(23)
aprobado.append(True)

#Agregar elemento y especificar la posicion
nombres.insert(1,'Pedro')
edades.insert(1,23)
aprobado.insert(1,True)


#Eliminar elementos de la listas 
nombres.remove('Juan')
#nombres.clear()



print('Cesar' in nombres)
print('Pedro' in nombres)
print(nombres.index('Pablo'))

#Cambiar posiciones
nombres[0]='Cesar'
edades[0] +=1