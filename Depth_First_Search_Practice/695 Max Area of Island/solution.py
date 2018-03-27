class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)  # y
        w = len(grid[0])  # x
        global w, h
        areas = []
        for i in range(h):  # y
            for j in range(w):  # x
                if grid[i][j] == 1:  # y x
                    parent = [Pos(j, i)]
                    visited = [Pos(j, i)]
                    return self.sum_area(parent, areas, grid, visited)
        return max(areas)

    def sum_area(self, parent, areas, grid, visited):
        area = 1
        while len(parent) != 0:
            for p in parent:
                if p not in visited:
                    visited.append(p)
                valid_child = []
                for n in self.neighbour(p):
                    if grid[n.y][n.x] == 1 and Pos(n.x, n.y) not in visited:
                        area += 1
                        valid_child.append(n)
                parent = valid_child
        areas.append(area)

    def neighbour(self, p):
        neighbours = []
        if p.x + 1 <= w:
            neighbours.append(Pos(p.x + 1, p.y))
        if p.x - 1 >= 0:
            neighbours.append(Pos(p.x - 1, p.y))
        if p.y + 1 <= h:
            neighbours.append(Pos(p.x, p.y + 1))
        if p.y - 1 >= 0:
            neighbours.append(Pos(p.x, p.y - 1))
        return neighbours


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y