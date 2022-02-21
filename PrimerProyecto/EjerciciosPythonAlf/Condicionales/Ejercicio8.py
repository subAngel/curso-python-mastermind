bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuacion: "))
#Clasificacion por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
#Mostrar nivel de puntuacion
if nivel =="":
    print("Esta puntuacion no es valida")
else:
    print("Tu nivel de rendimiento es ",nivel)
    print("te corresponde cobrar %.2f$" % (puntos*bonificacion))