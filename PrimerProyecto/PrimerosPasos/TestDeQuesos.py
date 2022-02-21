
titulo = "Bienvenido al test de Quesos"
print(titulo + "\n" + len(titulo)*"-" + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Que haces cuando ves una tabla de quesos?:\n" 
                "\tA - Salgo corriendo\n" 
                "\tB - Pruebo uno de los quesos o incluso varios\n" 
                "\tC - No puedo evitar devorarla")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Opcion incorrecta...")
    exit()

opcion = input("Pregunta 2: ¿Como te gusta la hamburguesa?:\n"
               "\tA - Sin queso\n"
               "\tB - Con queso\n"
               "\tC - Pan y queso")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Opcion incorrecta...")
    exit()

opcion  = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
                "\tA - Si\n"
                "\tB - A veces\n"
                "\tC - No")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Opcion incorrecta...")
    exit()


if puntuacion >= 25:
    print("felicidades, eres fanatico de los quesos")
elif puntuacion >= 15:
    print("Te agradan los quesos")
else:
    print("No eres fanatico de los quesos...")