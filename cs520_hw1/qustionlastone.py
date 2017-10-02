import numpy as np
import random
import matplotlib.pyplot as plt
import Maze
import DFS
import BFS
import AStar_Manhattan
import AStar_Euclidean

x = list(range(10))

dim = int(input ("Please enter a number indicating the dimension of maze: "))
prob_occ = float(input ("Please enter a number indicating the probability of disabled blocks: "))
y_BFS = list(range(10))
y_DFS = list(range(10))
for i in range(10):
    maze_matrix = np.zeros((dim, dim))
    num_disabled_blocks = int(np.floor(dim * dim * prob_occ) - 2)  # start and end shouldn't be occupied
    if num_disabled_blocks > 0:
        occ_block = random.sample(range(1, (dim * dim) - 1), num_disabled_blocks)
        occ_block = np.unravel_index(occ_block, (dim, dim))
        maze_matrix[occ_block] = 1
        maze_dict = Maze.build_maze(maze_matrix)
        result = BFS.bfs(maze_dict, dim, maze_matrix)
        y_BFS[i] = result["tree_size"]
        result = DFS.dfs(maze_dict, dim, maze_matrix)
        y_DFS[i] = result["tree_size"]

print y_BFS, y_DFS

plt.plot(x, y_BFS)
plt.plot(x, y_DFS)
plt.legend(['BFS', 'DFS'])
plt.show()