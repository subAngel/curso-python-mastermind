# Imagina que acabas de abrir na nueva cuenta de ahorros que te ofrece el 4% intereses
# al año. Estos ahorros debido a intereses, que no se cobran hasta final de año, se
# te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el
# usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras
# el primer, segundo y tercer año. Redondear cada cantidad a dos decimales.

interes = float(0.04)
cantidad = float(input("Ingrese la cantidad de dinero a ahorrar: "))
primer_ano = round(cantidad * (1+interes), 2)
segundo_ano = round( primer_ano * (1 + interes), 2)
tercer_ano = round(segundo_ano * (1 + interes), 2)
print("Ahorros en el primer año -> {}\n"
      "Ahorros en el segundo año -> {}\n"
      "Ahorros en el tercer año -> {}".format(primer_ano, segundo_ano, tercer_ano))