class Solution {
    public int removeDuplicates(int[] nums) {
        // 后一个数和前一个数比较
        if (nums == null || nums.length == 0) return 0;
        int count = 1;
        for (int i = 1; i< nums.length; i++) {
            if (nums[i - 1] != nums[i]) {
                // 通过count++ 实现删除
                nums[count++] = nums[i];
            }
        }
        return count;
    }
}
