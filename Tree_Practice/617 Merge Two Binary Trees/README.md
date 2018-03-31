#### 4 categories:

##### 1. t1 None & t2 None: -> return None

##### 2. t1 None t2 Tree -> return t2

##### 3. t2 None t1 Tree -> return t1

##### 4. t1 Tree t2 Tree<br />
###### Recursion:<br />

-> val = combined<br />
-> t.left = self.mergeTrees(t1.left,t2.left)<br />
-> t.right = self.mergeTrees(t1.right,t2.right)

#### Bugs to Note:

##### 1. Which is None and which is not None

##### 2. should have a return statement for the recursion function

##### 3. reduce redundancy to assign t1 or t2 directly to t

##### 4. can take t1 as the main tree to modify and return