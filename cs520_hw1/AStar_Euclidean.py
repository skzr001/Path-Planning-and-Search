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
    came_from = {}
    cost_so_far = {}
    came_from[(0, 0)] = None
    cost_so_far[(0, 0)] = 0
    count = 0
    while not visited.empty():
        current = visited.get()
        
        if current == destination:
            print ("A* with Euclidean distance has reached the destination")
            print ("Number of vertices visited: " + str(count+1))
            return maze_matrix_AE_visited
        
        for child, path in maze_dict[current]:
            new_cost = cost_so_far[current] + 1
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + dist_Euclidean(destination, child)
                visited.put(child, priority)
                count += 1
                maze_matrix_AE_visited[child] = -1
