import random
import numpy as np
import math

def build_maze(maze_matrix):
    maze_high, maze_width = maze_matrix.shape
    # print (mazeH,mazeW)

    maze_dict = {}

    for i in range(maze_high):
        for j in range(maze_width):
            if maze_matrix[i][j] == 0:
                maze_dict[(i, j)] = []

    #print('For loop version')
    #print (maze_dict)

    for i in range(maze_high):
        for j in range(maze_width):
            if maze_matrix[i][j] == 0:
                edge_up = ((i, j), 'Up')
                edgeS_down = ((i + 1, j), 'Down')
                edge_left = ((i, j), 'Left')
                edge_right = ((i, j + 1), 'Right')
                if i < maze_high - 1 and maze_matrix[i + 1][j] == 0:
                    maze_dict[(i, j)].append(edgeS)
                    maze_dict[(i + 1, j)].append(edgeN)
                if j < maze_width - 1 and maze_matrix[i][j + 1] == 0:
                    maze_dict[(i, j)].append(edgeE)
                    maze_dict[(i, j + 1)].append(edgeW)

    #print('------DICT----------')
    #print (maze_dict)

    return maze_dict

