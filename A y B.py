def compareTriplets(a, b):
    maxlen = max(len(a), len(b))  # Obtenemos la longitud máxima de las dos listas
    alice = 0
    bob = 0  # Puntuaciones iniciales
    for i in range(maxlen):  # Recorremos ambas listas en paralelo
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0 # cuando falten elementos este se remplaza a cero
        if ai > bi:
            alice += 1
        elif ai < bi:
            bob += 1
        # si son iguales, no hacemos nada
    return alice, bob  # Devolvemos las puntuaciones como una tupla
