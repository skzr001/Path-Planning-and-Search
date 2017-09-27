import numpy as np


def dfs(maze_dict, dim, maze_matrix):
    maze_matrix_dfs_visited = np.copy(maze_matrix)
    visited, stack = set(), [(0, 0)]
    destination = (dim-1, dim-1)

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            maze_matrix_dfs_visited[vertex] = -1
        else:
            continue

        if vertex == destination:
            print ("DFS has reached the destination")
            print ("Number of vertices visited: " + str(len(visited)))
            return maze_matrix_dfs_visited

        for child, path in maze_dict[vertex]:
            if child not in visited:
                stack.append(child)

    return "No result!"