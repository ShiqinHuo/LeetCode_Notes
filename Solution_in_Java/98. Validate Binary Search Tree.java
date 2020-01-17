class Solution {
    public boolean isValidBST(TreeNode root) {
        // dealing with the edge case
        if (root == null) return true;
        // stack for inorder tree search
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        while (root != null || !stack.isEmpty()) {
            // root 和 stack 非空
            while (root != null) {
                // root 不是空, 入栈
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (pre != null && root.val <= pre.val) return false;
            pre = root;
            root = root.right;
        }
        return true;
    }
}
