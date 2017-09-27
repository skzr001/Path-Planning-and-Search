import numpy as np
import math

def dist_manhattan(a, b):
    a_x, a_y = a
    b_x, b_y = b

    return math.fabs(a_x-b_x) + math.fabs(a_y-b_y)

