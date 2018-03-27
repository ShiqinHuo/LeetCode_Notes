### my initial idea
def pos class <br />
find neighbours <br />
check neighbours <br />
if not visited, accumulate the area, and return the max

### more sensible idea from [Penguin blog](https://www.polarxiong.com/archives/LeetCode-695-max-area-of-island.html)

#### 解法思路
这题就是典型的DFS啦，遍历矩阵，每当碰到1的时候就开始DFS，DFS每次碰到1就增加计数，然后把这个位置的值置为0，<br />DFS最后返回计数值，然后每次DFS返回值的最大值就是结果了。

有两点要注意的：

为了避免DFS重复计数，对于访问过的1，马上置为0即可。
注意到DFS是一个递归的过程，所以每一层只需要返回本身的计数（1）以及其子递归返回的计数（由此处出发DFS遍历到的1的个数）<br />的和就可以了。

##### 简洁解法！

[csdn blog](https://blog.csdn.net/wenqiwenqi123/article/details/78219709)<br />

def maxAreaOfIsland(self, grid):
     m, n = len(grid), len(grid[0])

     def dfs(i, j):
         if 0 <= i < m and 0 <= j < n and grid[i][j]:
             grid[i][j] = 0
             return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
         return 0

     areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
     return max(areas) if areas else 0