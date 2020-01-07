class Solution {
    public int firstMissingPositive(int[] nums) {
        
	int i = 0, n = nums.length;
	while (i < n) {
        // If the current value is in the range of (0,length) and it's not at its correct position, 
        // swap it to its correct position.
        // Else just continue;
		if (nums[i] >= 0 && nums[i] < n && nums[nums[i]] != nums[i])
			swap(nums, i, nums[i]);
		else
			i++;
	}
	int k = 1;

    // Check from k=1 to see whether each index and value can be corresponding.
	while (k < n && nums[k] == k)
		k++;

    // If it breaks because of empty array or reaching the end. K must be the first missing number.
	if (n == 0 || k < n)
		return k;
	else   // If k is hiding at position 0, K+1 is the number. 
		return nums[0] == k ? k + 1 : k;

    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
        
        
        // // O(n) time and uses O(1) space
        // // bucket sort 桶排序
        // if (nums == null || nums.length == 0) return 1;
        //  for (int i = 0; i < nums.length; i++) {
        //      // positive && less than the len 
        //      // index where it should be placed: nums[i] - 1
        //      if (nums[i] > 0 && nums[i] <= nums.length && nums[nums[i] - 1] != nums[i]) {
        //          int temp = nums[nums[i] - 1];
        //          nums[nums[i] - 1] = nums[i];
        //          nums[i] = temp;
        //          // not int the right index - swap 
        //      }
        //  }
        // for (int i = 0; i < nums.length; i++) {
        //     if (nums[i] != i + 1) {
        //         return i + 1;
        //     }
        // }
        // return nums.length + 1;
}
