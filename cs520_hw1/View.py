from Tkinter import *
import Maze
import time
import DFS
import BFS
import AStar_Euclidean
import AStar_Manhattan

# 我还没写完，别调试这个文件 By肖

default_dim = 10
default_prob_occ = 0.2

default_canvas_height = 600
default_canvas_width = 600

solver_choices = ['Deep First Search',
                  'Breadth First Search',
                  'A_Star with Euclidean Search',
                  'A_Star with Manhattan Search']

class Maze_simulation(object):
    def __init__(self):
        self.dim = default_dim
        self.prob_occ = default_prob_occ
        self.maze_matrix = Maze.random_maze(self.dim, self.prob_occ)

        self.window = Tk()
        self.window.title("Maze Simulation")
        self.window.geometry('+200+10')

        self.canvas = Canvas(self.window, bg="#ffffff", height=default_canvas_height, width=default_canvas_width)

        self.canvas.pack()

        self.draw_maze_matrix()

        self.map_edit_enabled = False
        self.fast_mode_enabled = False

        configWindow = Maze_simulation.prepare_configuration(self)
        self.selectedSolver = solver_choices[0]
        #self.selectedHardest = hardest_choices[0]

        configWindow.mainloop()
        self.window.mainloop()

    def draw_maze_matrix(self):
        tile_dim = (default_canvas_height - 20) / self.dim
        self.tiles = [[self.canvas.create_rectangle(10 + i * tile_dim, 10 + j * tile_dim,10 + (i + 1) * tile_dim, 10 + (j + 1) * tile_dim)
            for i in range(self.dim)] for j in range(self.dim)]

        for i in range(self.dim):
            for j in range(self.dim):
                if self.maze_matrix[i][j] == 1:
                    self.canvas.itemconfig(self.tiles[i][j], fill="#000000")

    def solver(self):
        print "Solve maze by " + self.selectedSolver
        start = time.time()
        if self.selectedSolver == solver_choices[0]:  # DFS
            maze_matrix_visited = DFS.dfs(self.maze_matrix)
        elif self.selectedSolver == solver_choices[1]:  # BFS
            maze_matrix_visited = BFS.bfs(self.maze_matrix)
        elif self.selectedSolver == solver_choices[2]:  # AStar with Euclidean
            maze_matrix_visited = AStar_Euclidean.a_star_search(self.maze_matrix)
        elif self.selectedSolver == solver_choices[3]:  # AStar with Manhattan
            maze_matrix_visited = AStar_Manhattan.a_star_search(self.maze_matrix)
        elapsed = (time.time() - start)
        print('Time elapsed: ', elapsed)
        if maze_matrix_visited != "No result!":
            self.visualizing(maze_matrix_visited)

    def draw_color(self, x, y, color='red'):
        self.canvas.itemconfig(self.tiles[x][y], fill=color)

    def visualizing(self, maze_matrix_visited):
        for i in range(self.dim):
            for j in range(self.dim):
                if maze_matrix_visited[i][j] != 1:
                    self.draw_color(i, j, 'white')
                elif maze_matrix_visited[i][j] == 1:
                    self.draw_color(i, j, 'black')

        for i in range(len(rs["record"])):
            loc = rs["record"][i]
            self.draw_color(loc.x, loc.y, 'yellow')
            time.sleep(0.05)
            self.window.update()
            if self.fastModeEnabled == True:
                for i in range(len(rs["record"])):
                    loc = rs["record"][i]
                    self.draw_color(loc.x, loc.y, 'yellow')
                for i in range(len(rs["solution"])):
                    loc = rs["solution"][i]
                    self.draw_color(loc.x, loc.y, 'blue')
                return
        for i in range(len(rs["solution"])):
            loc = rs["solution"][i]
            self.draw_color(loc.x, loc.y, 'blue')