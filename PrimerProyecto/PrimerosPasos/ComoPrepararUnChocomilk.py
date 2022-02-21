print("Voy a la cocina")
print("Abro el refri")

hay_leche = input("Hay leche? (S/N): ")
hay_chocomilk = input("Hay chocomilk? (S/N): ")

if hay_leche != "S" or hay_chocomilk != "S":
    print("Voy a la tienda...")
    if hay_leche != "S":
        print("Compro leche")
    if hay_chocomilk != "S":
        print("Compro Chocomilk")

print("Ponemos la leche en el vaso")
print("Ponemos el chocomilk en el vaso")
print("Mezclamos")
