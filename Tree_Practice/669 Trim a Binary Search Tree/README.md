### reference to Q.617

if lower_bound > node.val, trim the whole left, recursion with the right subtree

if upper_bound < node.val, trim the whole right, recursion with the left subtree

else:

root.left = trim(root.left)<br />
root.right = trim(root.right)

