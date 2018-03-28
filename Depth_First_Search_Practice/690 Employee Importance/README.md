[Leetcode discuss](https://leetcode.com/problems/employee-importance/discuss/112611/3-liner-Python-Solution-(beats-99))

#### Efficient idea
Simply convert the employees array/list into a map for easy lookup and then do a DFS traversal from the “root” <br />
employee node.

- Yangshun

#### Elegant solution

```python
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        dfs = lambda id: sum([dfs(sub_id) for sub_id in emps[id].subordinates]) + emps[id].importance
        return dfs(id)
```

