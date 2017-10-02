import numpy as np
import time

def bfs(maze_dict, dim, maze_matrix):  # maybe this is the most concise code
    maze_matrix_bfs_visited = np.copy(maze_matrix)
    start = time.time()
    path_dict = dict()
    visited, queue = set(), [(0, 0)]
    destination = (dim-1, dim-1)
    result = dict()

    max_fringe = 0
    num_fringe = 1

    while queue:
        max_fringe = max(max_fringe, num_fringe)
        vertex = queue.pop(0)  # notice the difference between DFS and BFS, queue and stack, and parameters
        num_fringe -= 1

        if vertex not in visited:
            visited.add(vertex)
            maze_matrix_bfs_visited[vertex] = -1
        else:
            continue

        if vertex == destination:
            #print ("BFS has reached the destination")
            #print ("Number of vertices visited: " + str(len(visited)))

            result["maze_path"] = find_path(path_dict, destination)
            result["maze_max_length"] = len(result["maze_path"])

            result["maze_solve_time"] = (time.time() - start)  # time to solve this maze
            #print ("Maze Path length is: " + str(len(result["maze_path"])))

            #print result["maze_path"]
            #print ("Maze Path length is: " + str(len(result["maze_path"])))
            result["tree_size"] = len(visited)
            result["max_fringe"] = max_fringe
            result["maze_matrix_visited"] = maze_matrix_bfs_visited
            #print ("Number of vertices visited: " + result["tree_size"])

            #return maze_matrix_bfs_visited
            return result

        for child, path in maze_dict[vertex]:
            if child not in visited:
                num_fringe += 1
                path_dict[child] = vertex
                queue.append(child)

    result['maze_max_length'] = -1
    result['tree_size'] = -1
    result['max_fringe'] = -1
    return  result
    #return "No result!"


def find_path(path_dict, destination):
    path = list()
    path.append(destination)
    current_node = destination

    while current_node != (0, 0):
        current_node = path_dict[current_node]
        path.append(current_node)

    return path