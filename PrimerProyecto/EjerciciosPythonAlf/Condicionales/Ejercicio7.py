rent = float(input("Cual es su renta anual? "))
tax_rate = None     # tipo impositivo
if rent < 10000:
    tax_rate = "5%"
elif 10000 <= rent < 20000:
    tax_rate = "10%"
elif 20000 <= rent < 35000:
    tax_rate = "15%"
elif 35000 <= rent < 60000:
    tax_rate = "30%"
elif rent >= 60000:
    tax_rate = "45%"
else:
    print("Tu renta tiene que ser un numero.")

print("Tu tipo impositivo es " + tax_rate)
