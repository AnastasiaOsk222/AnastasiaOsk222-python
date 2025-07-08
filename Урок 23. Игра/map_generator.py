import random

class MapGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [["empty" for _ in range(width)] for _ in range(height)]

    def generate_trees(self, count):
        for _ in range(count):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            self.map[y][x] = "tree"
        return self.map

    def generate_rivers(self, count):
        for _ in range(count):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            for _ in range(10):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.map[y][x] = "river"
                    dx, dy = random.choice([(-1,0),(1,0),(0,-1),(0,1)])
                    x += dx
                    y += dy
        return self.map

    def generate_special_cells(self, count, cell_type):
        for _ in range(count):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            if self.map[y][x] == "empty":
                self.map[y][x] = cell_type
        return self.map