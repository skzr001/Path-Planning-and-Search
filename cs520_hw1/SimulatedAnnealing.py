import random
import numpy as np
import math
import Maze
import DFS
import BFS
import AStar_Euclidean
import AStar_Manhattan
import copy



dim = 10
prob_occ = 0.6
property_num = 0
method_num = 3  # 0.DFS 1.BFS 2.A*Euclidean 3.A*Manhattan

def MethodChoose(method_num):

    if method_num == 0:
        method = DFS.dfs
    elif method_num == 1:
        method = BFS.bfs
    elif method_num == 2:
        method = AStar_Euclidean.a_stars_search
    elif method_num == 3:
        method = AStar_Manhattan.a_star_search
    return method

Method = MethodChoose(method_num)

while True:
    maze_0 = Maze.random_maze(dim, prob_occ)
    maze_dict_0 = Maze.build_maze(maze_0)
    result_0 = Method(maze_dict_0, dim, maze_0)
    if result_0['tree_size'] > 0:
        break


def mazeneighbor(matrix):
    mat = copy.copy(matrix)
    while True:
        i = random.randint(0, dim - 1)
        j = random.randint(0, dim - 1)
        if not((i==0 and j==0)or(i==(dim-1) and j==(dim-1))):
            break
    mat[i][j] = 0**mat[i][j]
    return mat


def probability(new,old):
        if(new > old):
            return 1.1
        return math.e**((new-old)/T)


# def solvable(matrix):
#     maze_dict = Maze.build_maze(matrix)
#     result = DFS.dfs(maze_dict, dim, matrix)
#     if result['tree_size'] > 0:
#         return True
#     return False


T = 10
Tmin = 0.1
r = 0.99
property = ['maze_max_length','tree_size','max_fringe']

while (T >= Tmin):

    maze_dict_0 = Maze.build_maze(maze_0)
    result_1 = Method(maze_dict_0, dim, maze_0)
    maze_N = mazeneighbor(maze_0)
    maze_dict_N = Maze.build_maze(maze_N)
    result_2 = Method(maze_dict_N, dim, maze_N)
    Probability = probability(result_2[property[property_num]], result_1[property[property_num]]);
    print (result_1[property[property_num]])

    if (result_2[property[property_num]] > 0):
        if (Probability > random.random()):
           # print("maze0=mazeN execute")
            maze_0 = maze_N
        else:
            print("give up new maze")
        T *= r
    else:
        print("unsolvable")

print (maze_0)





