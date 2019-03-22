class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h,w = len(grid),len(grid[0])

        def dfs(y,x):
            if 0<=y<h and 0<=x<w and grid[y][x]:
                grid[y][x]=0
                return 1 + dfs(y-1,x)+dfs(y+1,x)+dfs(y,x+1)+dfs(y,x-1)
            return 0
        areas = [dfs(y,x)for y in range(h) for x in range(w) if grid[y][x]]
        return max(areas) if areas else 0

## https://blog.csdn.net/wenqiwenqi123/article/details/78219709

#         h = len(grid)  # y
#         w = len(grid[0])  # x
#         areas = []
#         global w, h
#         for i in range(h):  # y
#             for j in range(w):  # x
#                 if grid[i][j] == 1:  # y x
#                     parent = [Pos(j, i)]
#                     grid[i][j] = 0
#                     return self.sum_area(parent, areas, grid)
#         return max(areas)
#
#     def sum_area(self, parent, areas, grid):
#         area = 1
#         while len(parent) != 0:
#             for p in parent:
#                 valid_child = []
#                 for n in self.neighbour(p):
#                     if grid[n.y][n.x] == 1:
#                         area += 1
#                         valid_child.append(n)
#                         grid[n.y][n.x] = 0
#                 parent = valid_child
#         areas.append(area)
#
#     def neighbour(self, p):
#         neighbours = []
#         if p.x + 1 <= w:
#             neighbours.append(Pos(p.x + 1, p.y))
#         if p.x - 1 >= 0:
#             neighbours.append(Pos(p.x - 1, p.y))
#         if p.y + 1 <= h:
#             neighbours.append(Pos(p.x, p.y + 1))
#         if p.y - 1 >= 0:
#             neighbours.append(Pos(p.x, p.y - 1))
#         return neighbours
#
#
# class Pos:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y