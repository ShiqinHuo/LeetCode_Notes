class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (target == nums[mid]) return mid;
            // 目标比中间小，mid当做end
            else if (target < nums[mid]) end = mid;
            // 目标比中间打，mid当做start
            else start = mid;
        }
        if (target <= nums[start]) {
            // target小于start,插入start位置
            return start;
        } else if (target <= nums[end]) {
            // target小于end大于start,插入start位置
            return end;
            
        // target大于end, 插入end后面一个
        } else return end + 1;
    }
}
