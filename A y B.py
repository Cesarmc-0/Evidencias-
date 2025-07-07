def compareTriplets(a, b):
    alice = bob = 0  # Puntuaciones iniciales

    for i in range(min(len(a),len(b))):  # Recorremos ambas listas en paralelo
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        # si son iguales, no hacemos nada
    return alice, bob
