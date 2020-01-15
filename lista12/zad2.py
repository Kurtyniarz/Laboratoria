import numpy as np


def normalize(float_array):
    normalized = np.linalg.norm(float_array)
    if normalized == 0:
        return float_array
    return float_array / normalized


newArray = []

while True:
    try:
        newArray.append(float(input()))
    except ValueError:
        break


for n in normalize(newArray):
    print(round(n, 5))
