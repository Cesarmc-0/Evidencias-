def serviceLane(width, queries):
    result = []
    for i, j in queries:
        result.append(min(width[i:j+1]))
    return result