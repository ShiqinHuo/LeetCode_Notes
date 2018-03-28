class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        else:
            h,w = len(grid),len(grid[0])

            def dfs(y, x):
                if 0<=y<h and 0<=x<w and grid[y][x] == "1":
                    grid[y][x] = "0"
                    return 1 + dfs(y-1,x)+dfs(y+1,x)+dfs(y,x+1)+dfs(y,x-1)
                return 0
            areas = [dfs(y,x) for x in range(w) for y in range(h) if grid[y][x] == "1" and dfs(y,x)!=0]
            return len(areas)
