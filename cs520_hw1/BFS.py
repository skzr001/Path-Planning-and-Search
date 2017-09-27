import numpy as np


def bfs(maze_dict, dim, maze_matrix):  # maybe this is the most concise code
    maze_matrix_bfs_visited = np.copy(maze_matrix)
    visited, queue = set(), [(0, 0)]
    destination = (dim-1, dim-1)

    while queue:
        vertex = queue.pop(0)  # notice the difference between DFS and BFS, queue and stack, and parameters
        if vertex not in visited:
            visited.add(vertex)
            maze_matrix_bfs_visited[vertex] = -1
        else:
            continue

        if vertex == destination:
            print ("BFS has reached the destination")
            print ("Number of vertices visited: " + str(len(visited)))
            return maze_matrix_bfs_visited

        for child, path in maze_dict[vertex]:
            if child not in visited:
                queue.append(child)

    return "No result!"

