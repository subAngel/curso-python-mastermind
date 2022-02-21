nombre = input('Como te llamas? ')
edad = int(input('Cuantos años tienes? '))
direccion = input('Cual es tu direccion? ')
telefono = input('Cual es tu numero de telefono? ')
persona = {'nombre': nombre, 'edad':edad, 'direccion': direccion, 'telefono':telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su numero telefonico es', persona['telefono'])