def compareTriplets(a, b):
    alice = bob = 0           # Puntuaciones iniciales
    for ai, bi in zip(a, b):  # Recorremos ambas listas en paralelo
        if ai > bi:
            alice += 1
        elif ai < bi:
            bob += 1
        # si son iguales, no hacemos nada
    return alice, bob