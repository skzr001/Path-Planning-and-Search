import numpy as np
import math


def dist_euclidean(a, b):
    a_x, a_y = a
    b_x, b_y = b

    return math.sqrt((a_x - b_x)*(a_x - b_x) + (a_y - b_y) * (a_y - b_y))

