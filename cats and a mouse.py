def catAndMouse(x, y, z):
    distA = abs(x - z)
    distB = abs(y - z)
    
    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"