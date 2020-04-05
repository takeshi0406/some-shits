
import numpy as np
from nptyping import Array


def foo(array: Array[np.float64]) -> str:
    return array


if __name__ == "__main__":
    #y = np.array([[1, 4, 4, 0], [2, 2, 4, 1]])
    x = None
    result = foo(x)
    print(result)
