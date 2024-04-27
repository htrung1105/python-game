from random import shuffle

class Maze:
    def __init__(self, rows=30, cols=40):
        self.rows = rows
        self.cols = cols
        self.keep_going = True

        self.maze = {}
        for y in range(rows):
            for x in range(cols):
                cell = {'south': 1, 'east': 1, 'visited': 0}
                self.maze[(x, y)] = cell

    def generate(self, cell):
        stack = []
        start_cell = self.maze[(self.cols - 1, self.rows - 1)]
        stack.append(start_cell)

        while stack:
            curr_cell = stack[-1]
            curr_cell['visited'] = 1

            neighbors = self.get_unvisited_neighbors(curr_cell)
            if neighbors:
                shuffle(neighbors)
                neighbor = neighbors[0]
                neighbor['visited'] = 1
                stack.append(neighbor)
                self.knock_wall(curr_cell, neighbor)
            else:
                stack.pop()

        self.keep_going = False

    def get_unvisited_neighbors(self, cell):
        neighbors = []
        (x, y) = self.get_coords(cell)

        north = (x, y - 1)
        south = (x, y + 1)
        east = (x + 1, y)
        west = (x - 1, y)

        if north in self.maze and self.maze[north]['visited'] == 0:
            neighbors.append(self.maze[north])
        if south in self.maze and self.maze[south]['visited'] == 0:
            neighbors.append(self.maze[south])
        if east in self.maze and self.maze[east]['visited'] == 0:
            neighbors.append(self.maze[east])
        if west in self.maze and self.maze[west]['visited'] == 0:
            neighbors.append(self.maze[west])

        return neighbors

    def knock_wall(self, cell, neighbor):
        xc, yc = self.get_coords(cell)
        xn, yn = self.get_coords(neighbor)

        if xc == xn and yc == yn + 1:
            neighbor['south'] = 0
        elif xc == xn and yc == yn - 1:
            cell['south'] = 0
        elif xc == xn + 1 and yc == yn:
            neighbor['east'] = 0
        elif xc == xn - 1 and yc == yn:
            cell['east'] = 0

    def get_coords(self, cell):
        coords = (-1, -1)
        for k in self.maze:
            if self.maze[k] is cell:
                coords = (k[0], k[1])
                break
        return coords

    def check_finished(self):
        for k in self.maze:
            if self.maze[k]['visited'] == 0:
                return False
        return True