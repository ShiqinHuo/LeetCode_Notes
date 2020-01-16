class Solution {
    /**
     time O(n)
     space O(n)
     method recursion
    */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        recursion(res, root);
        return res;
    }
    public void recursion(List<Integer> res, TreeNode root) {
        if (root == null) return;
        recursion(res, root.left);
        res.add(root.val);
        recursion(res, root.right);
    }
}
