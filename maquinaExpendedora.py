total=0

while True: 
    opcion= int(input("seleccione una bebida(1:cafe, 2:te, 3:jugo,):"))

    match opcion:
        case 1:
            print("cafe: $3.000")
            total += 3000
        
        case 2:
            print("te: $2.500")
            total += 2500

        case 3:
            print("jugo: $3.500")
            total += 3500

        case 0:
            print(f"total a pagar: $ {total}")

            break
        case _:
            print("opcion incorrecta")


