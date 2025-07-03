import random

jugador= []
banca= []


while True:
    juego= input("empezar el juego  SI/NO ").lower()

    if juego == "no":
        print("gracias por jugar")
        break
    elif juego == "si":
        cartaplayer= random.randint(1,13)
        cartabanca= random.randint(1,13)
        print(f"cartas banca {cartabanca}")
        print(f"cata jugador{cartaplayer}")

    if cartaplayer > cartabanca:
        print("gano")
        jugador.append(1)

    elif cartaplayer < cartabanca:
        print("perdio")
        banca.append(1)

    else:
        print("empate")

    if len(banca) == 3:
        print("ha perdido el juego")
        break

    elif len(jugador) ==5:
        print("ha ganado el juego")
        break
    print(f"gano {len(jugador)} veces y perdio {len(banca)} veces")
    print("gracias por jugar")