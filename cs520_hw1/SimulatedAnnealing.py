import random
import numpy as np
import math
import Maze
import DFS
import BFS
import AStar_Euclidean
import AStar_Manhattan
import copy
import matplotlib.pyplot as plt





def MethodChoose(method_num):

    if method_num == 'Deep First Search':
        method = DFS.dfs
    elif method_num == 'Breadth First Search':
        method = BFS.bfs
    elif method_num == 'A_Star with Euclidean Search':
        method = AStar_Euclidean.a_stars_search
    elif method_num == 'A_Star with Manhattan Search':
        method = AStar_Manhattan.a_star_search
    return method



def MazeBuild(Method, dim, prob_occ):
    while True:
        maze_0 = Maze.random_maze(dim, prob_occ)
        maze_dict_0 = Maze.build_maze(maze_0)
        result_0 = Method(maze_dict_0, dim, maze_0)
        if result_0['tree_size'] > 0:
           break
    return maze_0


def mazeneighbor(dim, matrix):
    mat = copy.copy(matrix)
    while True:
        i = random.randint(0, dim - 1)
        j = random.randint(0, dim - 1)
        if not((i==0 and j==0)or(i==(dim-1) and j==(dim-1))):
            break
    mat[i][j] = 0**mat[i][j]
    return mat


def probability(new, old, T):
        if(new > old):
            return 1.1
        return math.e**((new-old)/T)


# def solvable(matrix):
#     maze_dict = Maze.build_maze(matrix)
#     result = DFS.dfs(maze_dict, dim, matrix)
#     if result['tree_size'] > 0:
#         return True
#     return False




def SA(dim, method_num, property):
    T = 10000
    Tmin = 0.1
    r = 0.999
    # property = ['maze_max_length', 'tree_size', 'max_fringe']
    Result = list()
    Temperature = list()
    Method = MethodChoose(method_num)
    # dim = 10
    prob_occ = 0.6
    # method_num = 3  # 0.DFS 1.BFS 2.A*Euclidean 3.A*Manhattan
    maze_0 = MazeBuild(Method, dim, prob_occ)
    while (T >= Tmin):

        maze_dict_0 = Maze.build_maze(maze_0)
        result_1 = Method(maze_dict_0, dim, maze_0)
        maze_N = mazeneighbor(dim, maze_0)
        maze_dict_N = Maze.build_maze(maze_N)
        result_2 = Method(maze_dict_N, dim, maze_N)
        Probability = probability(result_2[property], result_1[property], T);
        Result.append(result_1[property])

        if (result_2[property] > 0):
            if (Probability > random.random()):
               # print("maze0=mazeN execute")
                maze_0 = maze_N

            Temperature.append(T)
            T *= r


    maze_dict_0 = Maze.build_maze(maze_0)
    result_1 = Method(maze_dict_0, dim, maze_0)
    # print(result_1[property[property_num]])
    #x = range(0, len(Result))
    #plt.figure()
    #plt.plot(x, Result)
    #plt.title(method_num + '\n' + property)
    #plt.show()
    return result_1

'''
method = ['Deep First Search','Breadth First Search','A_Star with Euclidean Search','A_Star with Manhattan Search']
property = ['maze_max_length','tree_size','max_fringe']

for i in range(0,4):
    M = method[i]
    for j in range(0,3):
        P = property[j]
        result = SA(10, M, P)
'''









