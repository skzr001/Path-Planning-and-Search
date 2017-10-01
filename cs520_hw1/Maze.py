import random
import numpy as np
import math


def random_maze(dim, prob_occ):
    maze_matrix = np.zeros((dim, dim))
    num_disabled_blocks = int(np.floor(dim*dim*prob_occ)-2)
    if num_disabled_blocks > 0:
        occ_block = random.sample(range(1, (dim * dim) - 1), num_disabled_blocks)
        occ_block = np.unravel_index(occ_block, (dim, dim))
        maze_matrix[occ_block] = 1

    return maze_matrix


def build_maze(maze_matrix):
    maze_high, maze_width = maze_matrix.shape
    # print (mazeH,mazeW)

    maze_dict = {}

    for i in range(maze_high):
        for j in range(maze_width):
            if maze_matrix[i][j] == 0:
                maze_dict[(i, j)] = []

    #print('For loop version')
    print (maze_dict)

    for i in range(maze_high):
        for j in range(maze_width):
            if maze_matrix[i][j] == 0:
                edge_up = ((i, j), 'Up')
                edge_down = ((i + 1, j), 'Down')
                edge_left = ((i, j), 'Left')
                edge_right = ((i, j + 1), 'Right')
                if i < maze_high - 1 and maze_matrix[i + 1][j] == 0:
                    maze_dict[(i, j)].append(edge_down)
                    maze_dict[(i + 1, j)].append(edge_up)
                if j < maze_width - 1 and maze_matrix[i][j + 1] == 0:
                    maze_dict[(i, j)].append(edge_right)
                    maze_dict[(i, j + 1)].append(edge_left)

    #print('------DICT----------')
    #print (maze_dict)

    return maze_dict

