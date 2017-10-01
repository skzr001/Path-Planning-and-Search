import numpy as np
import math
import heapq

def dist_Euclidean(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)



class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __getitem__(self, key):
        return self[key]
    
    def __len__(self):
        return len(self.elements)


def a_star_search(maze_dict, dim, maze_matrix):
    maze_matrix_AE_visited = np.copy(maze_matrix)
    visited = PriorityQueue()
    visited.put((0, 0), 0)
    destination = (dim - 1, dim - 1)
    path_dict = {}
    path_dict[(0, 0)] = (0, 0)
    result = dict()
    result["status"] = -1
    max_fringe = 0
    num_fringe = 1
    cost_so_far = {}
    cost_so_far[(0, 0)] = 0
    count = 0

    while not visited.empty():
        max_fringe = max(max_fringe, num_fringe)
        current = visited.get()
        num_fringe = 1
        if current == destination:

            # print ("Number of vertices visited: " + str(count+1))
            print ("Congratulations! A* with Euclidean distance has reached the destination!")
            result["maze_path"] = find_path(path_dict, destination)
            result["maze_max_length"] = len(result["maze_path"])
            # print ("Maze path is: ")
            print result["maze_path"]
            print ("Maze Path length is: " + str(len(result["maze_path"])))
            result["tree_size"] = str(count)
            result["max_fringe"] = max_fringe
            result["maze_matrix_visited"] = maze_matrix_AE_visited
            print ("Number of vertices visited: " + result["tree_size"])
            print ("Number of Max fringe: " + str(result["max_fringe"]))
            return maze_matrix_AE_visited
        
        for child, path in maze_dict[current]:
            new_cost = cost_so_far[current] + 1
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + dist_Euclidean(destination, child)
                visited.put(child, priority)
                count += 1
                num_fringe += 1
                path_dict[child] = current
                maze_matrix_AE_visited[child] = -1

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