reference:
[bookshadow LeetCode解题报告]（http://bookshadow.com/weblog/2017/01/22/leetcode-predict-the-winner/）

## 解题思路：
### Alpha-Beta搜索 + 记忆化

函数solve(nums)计算当前玩家从nums中可以获得的最大收益，当收益>=0时，此玩家获胜
### First step analysis:
solve(nums) = max(nums[0] - solve(nums[1:]), nums[-1] - solve(nums[:-1]))

