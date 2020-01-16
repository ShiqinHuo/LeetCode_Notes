class Solution {
    // recursive solution
    public List<TreeNode> generateTrees(int n) {
        if (n < 1) return new ArrayList<>();
        return generateTrees(1, n);
    }
    
    public List<TreeNode> generateTrees(int low, int high) {
        List<TreeNode> ans = new ArrayList<>();
        if (low > high) {
            ans.add(null);
            return ans;
        }
        for (int i = low; i <= high; i++) {
            List<TreeNode> leftSubtrees = generateTrees(low, i -1);
            List<TreeNode> rightSubtrees = generateTrees(i + 1, high);
            for (TreeNode leftSubtree : leftSubtrees) {
                for (TreeNode rightSubtree : rightSubtrees) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftSubtree;
                    root.right = rightSubtree;
                    ans.add(root);
                }
            }
        }
        return ans;
    }
}
