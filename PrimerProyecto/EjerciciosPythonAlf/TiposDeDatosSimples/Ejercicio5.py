# Escribir un programa que pregutne al usuario por el n[umero de horas trabajadas y el
# coste por hora. Despues debe mostrar por pantalla la paga que le corresponde
num_horas = int(input("Cuantas horas trabajas? "))
coste_hora = int(input("A cuanto te pagan la hora? "))
print("Tu sueldo es {}".format(num_horas*coste_hora))