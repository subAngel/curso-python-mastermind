# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
# el indice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
# 'Tu índice de masa corporal es <imc>' donde imd es el índice de masa corporal caldulado
# redondeado con 2 decimales
peso = int(input("Cuanto pesas (kg)? "))
estatura = float(input("Cuanto mides (m)? "))
imc = (peso)/(estatura**2)
print("Tu índice de masa corporal es {}".format(round(imc,2)))