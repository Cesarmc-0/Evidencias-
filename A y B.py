def compareTriplets(a, b):
    alice = bob = 0  # Puntuaciones iniciales
    min = min(len(a,b))
    for ai, bi in range(min):  # Recorremos ambas listas en paralelo
        if ai > bi:
            alice += 1
        elif ai < bi:
            bob += 1
        # si son iguales, no hacemos nada
    return alice, bob
