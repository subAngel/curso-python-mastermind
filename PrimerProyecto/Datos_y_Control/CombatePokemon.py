from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

TAMANIO_BARRA_VIDA = 20

vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_actual_squirtle > 0 and vida_actual_pikachu > 0:
    # Se desenvuelven los turnos del combate

    # Turno de pikachu
    print("-----------------")
    print("Turno del Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con bola voltio")
        vida_actual_squirtle -= 10
    else:
        # Impactrueno
        print("Pikachu ataca con impactrueno")
        vida_actual_squirtle -= 9

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0
    if vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    barra_vida_pikachu = int(vida_actual_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    barra_vida_squirtle = int(vida_actual_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)

    print("VIDA DE PIKACHU \t-->\t [{}{}] {}/{}".format("#" * barra_vida_pikachu,
                                                        " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),
                                                        vida_actual_pikachu, VIDA_INICIAL_PIKACHU))
    print("VIDA DE SQUIRTLE \t-->\t [{}{}] {}/{}".format("#" * barra_vida_squirtle,
                                                         " " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle),
                                                         vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n")
    os.system("cls")

    # Turno Squirtle

    print("--------------")
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola de [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_actual_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de agua")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_actual_pikachu -= 9
    elif ataque_squirtle == "N":
        print("SQUIRTLE no hace nada...")

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0
    if vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    barra_vida_pikachu = int(vida_actual_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    barra_vida_squirtle = int(vida_actual_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)

    print("VIDA DE PIKACHU \t-->\t [{}{}] {}/{}".format("#" * barra_vida_pikachu,
                                                        " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),
                                                        vida_actual_pikachu, VIDA_INICIAL_PIKACHU))
    print("VIDA DE SQUIRTLE \t-->\t [{}{}] {}/{}".format("#" * barra_vida_squirtle,
                                                         " " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle),
                                                         vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n")
    os.system("cls")

if vida_actual_pikachu > vida_actual_squirtle:
    print("\t\nEl Ganador es PIKACHU")
elif vida_actual_squirtle > vida_actual_pikachu:
    print("\t\nEl Ganador es SQUIRTLE")
else:
    print("EMPATE")
