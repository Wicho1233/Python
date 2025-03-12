import pandas as pd
#Ingresar los datos manualmente en un diccionario
datos = {
    'Nombre':['Carlos','Ana','Luis','Maria'],
    'Edad':[23,34,23,44],
    'Ciudad':['Mexico','Peru','Alemania','EEUU']
}

tabla = pd.DataFrame(datos)

print(tabla)