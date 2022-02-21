# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido de la inversión

inversion = int(input("Cuanto dinero va a invertir? "))
interes = float(input("Cuanto es el interes anual? "))
years = int(input("Por cuantos años? "))
capital = round(inversion * (interes / 100 + 1) ** years, 2)
print("Capital final -> {}".format(capital))