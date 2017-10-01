import numpy as np
import time



def dfs(maze_dict, dim, maze_matrix):
    maze_matrix_dfs_visited = np.copy(maze_matrix)
    start = time.time()

    path_dict = dict()
    path_dict[(0, 0)] = (0, 0)

    visited, stack = set(), [(0, 0)]
    destination = (dim-1, dim-1)
    result = dict()

    # set required return value for HW1
    result["status"] = -1
    max_fringe = 0
    num_fringe = 1

    while stack:
        max_fringe = max(max_fringe, num_fringe)
        vertex = stack.pop()
        num_fringe -= 1

        if vertex not in visited:
            visited.add(vertex)
            maze_matrix_dfs_visited[vertex] = -1
        else:
            continue

        if vertex == destination:
            #path_dict[destination] = vertex  #  this stupid mistake waste my whole night. Damn it!
            print ("Congratulations! DFS has reached the destination!")
            result["maze_path"] = find_path(path_dict, destination)
            result["maze_max_length"] = len(result["maze_path"])
            result["maze_solve_time"] = (time.time() - start)  # time to solve this maze
            print ("running time is: " + str(result["maze_solve_time"]))
            #print ("Maze path is: ")
            print result["maze_path"]
            print ("Maze Path length is: " + str(len(result["maze_path"])))
            result["tree_size"] = str(len(visited))
            result["max_fringe"] = max_fringe
            result["maze_matrix_visited"] = maze_matrix_dfs_visited

            print ("Number of vertices visited: " + result["tree_size"])
            #return maze_matrix_dfs_visited
            return result

        for child, path in maze_dict[vertex]:
            if child not in visited:
                num_fringe += 1
                path_dict[child] = vertex
                #print ("vertex")
                #print vertex
                #print ("child")
                #print child
                #print ("path_dict[child]")
                #print path_dict[child]
                stack.append(child)

    return "No Result!"


def find_path(path_dict, destination):
    path = list()
    path.append(destination)
    current_node = destination

    while current_node != (0, 0):
        #print ("current node" + str(current_node))
        current_node = path_dict[current_node]
        #print ("Parent of current node" + str(current_node))
        path.append(current_node)

    return path