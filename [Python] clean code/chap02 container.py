class Boundaris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaris(width, height)

    def __contains__(self, coord):
        return coord in self.limits

grid = Grid(10,10)
coord = (1,1)
if coord in grid:
    print('Yes')
else:
    print('No')