from Tkinter import *
import Maze
import time
import DFS
import BFS
import AStar_Euclidean
import AStar_Manhattan
import SimulatedAnnealing
import numbers

default_dim = 10
default_prob_occ = 0.2

default_canvas_height = 600
default_canvas_width = 600

solver_choices = ["Deep First Search",
                  "Breadth First Search",
                  "A_Star with Euclidean Search",
                  "A_Star with Manhattan Search"]

hard_choices = ["maze_max_length", "tree_size", "max_fringe"]


class Maze_simulation(object):
    def __init__(self):
        self.dim = default_dim
        self.prob_occ = default_prob_occ
        self.maze_matrix = Maze.random_maze(self.dim, self.prob_occ)
        self.maze_dict = Maze.build_maze(self.maze_matrix)

        self.window = Tk()
        self.window.title("Maze Simulation")
        self.window.geometry('+200+10')

        # SA window
        self.SA_window = Tk()
        self.SA_window.title("Simulated Annealing")
        self.SA_window.geometry('+200+10')

        # Sa canvas
        self.SA_canvas = Canvas(self.SA_window, bg="#ffffff", height=default_canvas_height, width=default_canvas_width)
        self.SA_canvas.pack()
        # Window Canvas
        self.canvas = Canvas(self.window, bg="#ffffff", height=default_canvas_height, width=default_canvas_width)
        self.canvas.pack()

        self.draw_maze_matrix()
        self.draw_SA_matrix()


        self.map_edit_enabled = False
        self.fast_mode_enabled = False

        self.select_hard = hard_choices[0]

        configWindow = Maze_simulation.prepare_configuration(self)
        self.selectedSolver = solver_choices[0]
        #self.selectedHardest = hardest_choices[0]

        configWindow.mainloop()
        self.SA_window.mainloop()
        self.window.mainloop()


    def draw_maze_matrix(self):
        tile_dim = (default_canvas_height - 20) / self.dim
        self.tiles = [[self.canvas.create_rectangle(10 + i * tile_dim, 10 + j * tile_dim,10 + (i + 1) * tile_dim, 10 + (j + 1) * tile_dim)
            for i in range(self.dim)] for j in range(self.dim)]

        for i in range(self.dim):
            for j in range(self.dim):
                if self.maze_matrix[i][j] == 1:
                    self.canvas.itemconfig(self.tiles[i][j], fill="#000000")

    def draw_SA_matrix(self):
        tile_dim = (default_canvas_height - 20) / self.dim
        self.tiles = [[self.SA_canvas.create_rectangle(10 + i * tile_dim, 10 + j * tile_dim,10 + (i + 1) * tile_dim, 10 + (j + 1) * tile_dim)
            for i in range(self.dim)] for j in range(self.dim)]

        for i in range(self.dim):
            for j in range(self.dim):
                if self.maze_matrix[i][j] == 1:
                    self.SA_canvas.itemconfig(self.tiles[i][j], fill="#000000")

    def solver(self):
        #print "Solve maze by " + self.selectedSolver
        start = time.time()
        if self.selectedSolver == solver_choices[0]:  # DFS
            maze_matrix_visited = DFS.dfs(self.maze_dict, self.dim, self.maze_matrix)
        elif self.selectedSolver == solver_choices[1]:  # BFS
            maze_matrix_visited = BFS.bfs(self.maze_dict, self.dim, self.maze_matrix)
        elif self.selectedSolver == solver_choices[2]:  # AStar with Euclidean
            maze_matrix_visited = AStar_Euclidean.a_stars_search(self.maze_dict, self.dim, self.maze_matrix)
        elif self.selectedSolver == solver_choices[3]:  # AStar with Manhattan
            maze_matrix_visited = AStar_Manhattan.a_star_search(self.maze_dict, self.dim, self.maze_matrix)
        elapsed = (time.time() - start)
        # print('Time elapsed: ', elapsed)
        if maze_matrix_visited != "No result!":
            self.visualizing(maze_matrix_visited)

    def draw_color(self, x, y, color='red'):
        self.canvas.itemconfig(self.tiles[x][y], fill=color)

    def draw_SA_color(self, x, y, color='red'):
        self.SA_canvas.itemconfigure(self.tiles[x][y], fill=color)


    def visualizing(self, maze_matrix_visited):
        maze_solved = maze_matrix_visited["maze_matrix_visited"]
        for i in range(self.dim):
            for j in range(self.dim):
                if maze_solved[i][j] != 1:
                    self.draw_color(i, j, 'white')
                elif maze_solved[i][j] == 1:
                    self.draw_color(i, j, 'black')

        for i in range(self.dim):
            for j in range(self.dim):
                if maze_solved[i][j] == -1:
                    self.draw_color(i, j, 'yellow')

        # Maybe I shouldn't store vertex in form (x,y)
        # Stupid decision waste my too many time
        for i in (maze_matrix_visited["maze_path"]):
            x = i[0]
            y = i[1]
            self.draw_color(x, y, 'green')

    def SA_visualizing(self, maze_matrix_visited):
        maze_solved = maze_matrix_visited["maze_matrix_visited"]
        print maze_solved
        for i in range(self.dim):
            for j in range(self.dim):
                if maze_solved[i][j] != 1:
                    self.draw_SA_color(i, j, 'white')
                elif maze_solved[i][j] == 1:
                    self.draw_SA_color(i, j, 'black')
        print ("SA draw")

        for i in range(self.dim):
            for j in range(self.dim):
                if maze_solved[i][j] == -1:
                    self.draw_SA_color(i, j, 'yellow')

        for i in (maze_matrix_visited["maze_path"]):
            x = i[0]
            y = i[1]
            self.draw_SA_color(x, y, 'green')

        print ("SA draw")

    def prepare_configuration(resp):
        print "Show configuration"
        root = Tk()
        # Reset button
        carTypeBtn = Button(root, text="Reset simulator",
                            command=resp.reset_simulator)
        carTypeBtn.pack()
        # Tile Edit On/Off Switch
        mapEditBtn = Button(root, text="Map Edit: Off",
                            command=resp.enable_edit)
        mapEditBtn.pack()
        resp.mapEdit = mapEditBtn
        # Maze Dimensions
        nDimLabel = Label(root, text="Number of dimensions")
        nDimLabel.pack()
        nDimEntry = Entry(root, justify='center',
                          textvariable=StringVar(root, value=str(default_dim)))
        nDimEntry.pack()
        resp.nDimEntry = nDimEntry

        # Block Probability
        probLabel = Label(root, text="Probability of block tiles")
        probLabel.pack()
        probEntry = Entry(root, justify='center',
                          textvariable=StringVar(root, value=str(default_prob_occ)))
        probEntry.pack()
        resp.probEntry = probEntry

        # Run Solver
        solverLabel = Label(root, text="Choose the solver")
        solverLabel.pack()
        tkvar = StringVar(root, value=solver_choices[0])
        tkvar.trace('w', lambda *args: resp.changeSolver(tkvar.get()))
        solverOption = OptionMenu(root, tkvar, *solver_choices)
        solverOption.pack()
        solverBtn = Button(root, text="Solve", command=resp.solver)
        solverBtn.pack()

        #SA button
        hardLabel = Label(root, text="Choose a property")
        hardLabel.pack()
        tkvar2 = StringVar(root, value=hard_choices[0])
        tkvar2.trace('w', lambda *args: resp.changeHard(tkvar2.get()))
        hardestOption = OptionMenu(root, tkvar2, *hard_choices)
        hardestOption.pack()
        SABtn = Button(root, text="simAnnealing", command=resp.run_SA)
        SABtn.pack()

        return root

    def run_SA(self):
        print "Solve hard maze by " + self.selectedSolver
        start = time.time()
        maze_matrix_visited = SimulatedAnnealing.SA(self.dim, self.selectedSolver, self.select_hard)
        elapsed = (time.time() - start)
        # print('Time elapsed: ', elapsed)
        if maze_matrix_visited != "No result!":
            self.SA_visualizing(maze_matrix_visited)

    def reset_simulator(self):
        self.mapEditEnabled = False

        self.maze_matrix = Maze.random_maze(self.dim, self.prob_occ)
        self.maze_dict = Maze.build_maze(self.maze_matrix)
        self.canvas.delete("all")
        self.SA_canvas.delete("all")
        self.draw_maze_matrix()
        self.draw_SA_matrix()
        pass

    def enable_edit(self):
        if self.map_edit_enabled == False:
            self.map_edit_enabled = True
            self.mapEdit.config(text="Map Edit: On")
        else:
            self.changeMap()
            self.map_edit_enabled = False
            self.mapEdit.config(text="Map Edit: Off")


    def changeMap(self):
        print "Update map"
        self.changeNDim()
        self.changeProb()
        self.maze_matrix = Maze.random_maze(self.dim, self.prob_occ)
        self.canvas.delete("all")
        self.SA_canvas.delete("all")
        self.draw_maze_matrix()
        self.draw_SA_matrix()

    def changeNDim(self):
        print "Change the number of rows"
        entry = self.nDimEntry
        nDim = entry.get()
        if not nDim.isdigit() or self.map_edit_enabled == False:
            entry.delete(0, END)
            entry.insert(0, str(self.dim))
        else:
            self.dim = int(nDim)

    def changeProb(self):
        entry = self.probEntry
        p = entry.get()
        if isinstance(p, numbers.Number) or self.map_edit_enabled == False:
            entry.delete(0, END)
            entry.insert(0, str(self.prob_occ))
        else:
            self.prob_occ = float(p)

    def changeSolver(self, item):
        print "Change solver to: " + item
        self.selectedSolver = item

    def changeHard(self, item):
        print "Change property to: " + item
        self.select_hard = item

ms = Maze_simulation()