fecha = input("Escribe una fecha [dd/mm/aaaa]: ")

meses = {'01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril', '05': 'Mayo', '06': 'Junio',
         '07': 'Julio', '08': 'Agosto', '09': 'Septiembre', '10': 'Octubre', '11': 'Noviembre', '12': 'Diciembre'}

fecha_dividida = fecha.split('/')
dia = fecha_dividida[0]
mes = meses[fecha_dividida[1]]
year = fecha_dividida[2]

print("{} de {} del {}".format(dia, mes, year))