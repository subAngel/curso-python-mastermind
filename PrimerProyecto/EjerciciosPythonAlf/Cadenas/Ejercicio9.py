# MI SOLUCION
fec_nac = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
fec_nac = fec_nac.split("/")

print("Naciste el dia {} del mes {} del anio {}".format(fec_nac[0], fec_nac[1], fec_nac[2]))

# SOLUCION PAGINA
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)