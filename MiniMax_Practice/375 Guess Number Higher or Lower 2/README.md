### work out like Q.374
to find the guarantee, we have to assume the worst case for Q.374 program
<br />assume the mid is lower (picked number is higher), we accumulate the mid into sum
<br />s = 0
<br />s = 0 + (1+n)/2, left = (1+n)/2 + 1, mid = ((3+n)/2 + n)/2 =
<br />recursion until if n - left == 4 ---> add mid
<br />if n - left == 3 ----> add mid

<br />Done!

### Recursion:
s += mid until (n - left) == 3 or (n - left) == 4



###解题思路[bookshadow题解](http://bookshadow.com/weblog/2016/07/16/leetcode-guess-number-higher-or-lower-ii/)：

动态规划（Dynamic Programming）

参考：[leetcode disscuss](https://discuss.leetcode.com/topic/51356/two-python-solutions)

状态转移方程：

dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]))

其中dp[i][j]表示猜出范围[i, j]的数字需要花费的最少金额。