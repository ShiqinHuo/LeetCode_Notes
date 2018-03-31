####4 categories:

#####1. t1 None & t2 None: -> return None

#####2. t1 None t2 Tree -> return t2

#####3. t2 None t1 Tree -> return t1

#####4. t1 Tree t2 Tree<br />
######Recursion:<br />

-> val = combined
-> t.left = self.mergeTrees(t1.left,t2.left)<br />
-> t.right = self.mergeTrees(t1.right,t2.right)