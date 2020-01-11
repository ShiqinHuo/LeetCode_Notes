class Solution {
    public int thirdMax(int[] nums) {
        Integer max_num = null;
        Integer second_max = null;
        Integer third_max = null;
        
        for (Integer num : nums) {
            if (num.equals(max_num) || num.equals(second_max) || num.equals(third_max)) {
                continue;
            }
            if (max_num == null || num > max_num) {
                third_max = second_max;
                second_max = max_num;
                max_num = num;
            } else if (second_max == null || num > second_max) {
                third_max = second_max;
                second_max = num;
            } else if (third_max == null || num > third_max) {
                third_max = num;
            }
        }
        if (third_max == null) return max_num;
        return third_max;
    }
}
