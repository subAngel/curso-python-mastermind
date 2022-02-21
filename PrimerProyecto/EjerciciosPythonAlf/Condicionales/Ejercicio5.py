edad = int(input("Intoduzca su edad: "))
ingresos_mensuales = float(input("Cual es su ingreso mensual? "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Ya puedes tributar impuestos")
else:
    print("No puedes tributar")