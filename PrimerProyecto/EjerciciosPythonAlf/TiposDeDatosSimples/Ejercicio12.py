# Una panadería vende barras de pan a 3.49 dolares cada una. El pan que no es del día tiene un
# descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas
# que no son del día. Después el programa debe mostrar el precio habitual de una barra  de pan,
# el descuento que se le hace por no ser fresca y el coste final total.

precio_pan = 3.49
descuento = 0.6
panes_vendidos = int(input("Cuantos panes que no son del dia se vendieron? "))
total = round((panes_vendidos * precio_pan) * descuento, 2)
print("Panes vendidos \t-> \t {}\n"
      "Precio normal \t->\t {}$\n"
      "Descuento \t\t->\t {}%\n"
      "--------------------------\n"
      "TOTAL \t\t\t->\t {}$".format(panes_vendidos, round(precio_pan*panes_vendidos, 2), descuento*100, total))