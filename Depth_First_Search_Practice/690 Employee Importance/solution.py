"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp_dic = {emp.id: emp for emp in employees}

        def dfs(id):
            importance = emp_dic[id].importance + sum(dfs(sub_id) for sub_id in emp_dic[id].subordinates)
            return importance

        return dfs(id)

# https://leetcode.com/problems/employee-importance/discuss/112611/3-liner-Python-Solution-(beats-99)