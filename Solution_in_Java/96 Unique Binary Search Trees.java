class Solution {
    public int numTrees(int n) {
        // dynamic programming
        // 判断数量或者是boolean可以考虑DP
        if (n < 1) return 0;
        int[] nums = new int[n + 1];
        nums[0] = 1;
        nums[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                nums[i] += (nums[i-j-1]*nums[j]);
            }
        }
        return nums[n];
    }
}
