diccionario = {'a': 10, 'b': 15, 'c': "hola", 2: "mundo", 'b': 20}

diccionario['nueva clave'] = "nuevo elemento"

diccionario['a'] = True

del diccionario['c']

valores = list(diccionario.values())    # Convierte el diccionario en una lista ()
otros_valores = tuple(diccionario.values()) # Convierte el diccionario en una tupla []
claves = list(diccionario.keys())   # Convierte las claves del diccionario en una lista


print(diccionario)

print(diccionario['a'])

print(diccionario.values()) #Aqui unicamente muestra los valores

print(diccionario.keys())   #Aqui solo muestra las llaves/claves

print(diccionario.items())  #convierte el diccionario en una tupla

print(valores)

print(otros_valores)

print (claves)