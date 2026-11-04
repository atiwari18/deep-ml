import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    c: list[list[int|float]] = []

    if np.size(a, axis=1) != np.size(b, axis=0):
        return -1
    else:
        for row in a:
            temp = []
            for tuple in zip(*b):
                temp.append(np.dot(row, list(tuple)))
            
            c.append(temp)

    return c