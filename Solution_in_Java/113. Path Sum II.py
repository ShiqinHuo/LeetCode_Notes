# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)

def pathSum(self, root, sum):
    if not root:
        return []
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        self.dfs(root.right, sum-root.val, ls+[root.val], res)
        
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
    return [[root.val]+i for i in tmp]

# BFS + queue    
def pathSum3(self, root, sum): 
    if not root:
        return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        curr, val, ls = queue.pop(0)
        if not curr.left and not curr.right and val == sum:
            res.append(ls)
        if curr.left:
            queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
        if curr.right:
            queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
    return res
    
# DFS + stack I  
def pathSum4(self, root, sum): 
    if not root:
        return []
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res 

# DFS + stack II   
def pathSum5(self, root, s): 
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        curr, ls = stack.pop()
        if not curr.left and not curr.right and sum(ls) == s:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, ls+[curr.left.val]))
    return res

######################## shorten below ###############################

def pathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, path, res):
    if root:
        if sum == root.val and not root.left and not root.right:
            res.append(path+[root.val])
        self.dfs(root.left, sum-root.val, path+[root.val], res)
        self.dfs(root.right, sum-root.val, path+[root.val], res)
        
def pathSum2(self, root, sum):
    res, stack = [], [(root, sum, [])]
    while stack:
        node, sum, path = stack.pop()
        if node:
            if node.val == sum and not node.left and not node.right:
                res.append(path+[node.val])
            stack.append((node.right, sum-node.val, path+[node.val]))
            stack.append((node.left, sum-node.val, path+[node.val]))
    return res
    
def pathSum(self, root, sum):
    res, queue = [], collections.deque([(root, sum, [])])
    while queue:
        node, sum, path = queue.popleft()
        if node:
            if node.val == sum and not node.left and not node.right:
                res.append(path+[node.val])
                continue
            queue.append((node.left, sum-node.val, path+[node.val]))
            queue.append((node.right, sum-node.val, path+[node.val]))
    return res
