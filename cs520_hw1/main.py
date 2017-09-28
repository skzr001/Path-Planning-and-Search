import random
import numpy as np
import math
import Maze
import DFS
import BFS
import AStar_Manhattan
import AStar_Euclidean

dim = int(input ("Please enter a number indicating the dimension of maze: "))
maze_matrix = np.zeros((dim, dim))
prob_occ = float(input ("Please enter a number indicating the probability of disabled blocks: "))
print (maze_matrix)

num_disabled_blocks = int(np.floor(dim*dim*prob_occ)-2)  # start and end shouldn't be occupied
if num_disabled_blocks > 0:
    occ_block = random.sample(range(1, (dim*dim)-1), num_disabled_blocks)
    occ_block = np.unravel_index(occ_block, (dim, dim))
    maze_matrix[occ_block] = 1

print(maze_matrix)

maze_dict = Maze.build_maze(maze_matrix)


# Notice that BFS and DFS not the same as original version, we just need a route from START to END
# show DFS
maze_matrix_dfs_visited = DFS.dfs(maze_dict, dim, maze_matrix)
print maze_matrix_dfs_visited

# show_BFS
maze_matrix_bfs_visited = BFS.bfs(maze_dict, dim, maze_matrix)
print maze_matrix_bfs_visited


# show_AStar_Manhattan
maze_matrix_AM_visited = AStar_Manhattan.a_star_search(maze_dict, dim, maze_matrix)
print maze_matrix_AM_visited


# show_AStar_Euclidean
maze_matrix_AE_visited = AStar_Euclidean.a_star_search(maze_dict, dim, maze_matrix)
print maze_matrix_AE_visited