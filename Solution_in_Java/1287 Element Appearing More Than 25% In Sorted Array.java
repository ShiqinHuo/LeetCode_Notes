class Solution {
    public int findSpecialInteger(int[] arr) {
        int len = arr.length/4;
        // System.out.println("len: " + String.valueOf(len));
        int count = 1;
        for (int pointer = 0; pointer < arr.length - 1; pointer++){
            if (arr[pointer + 1] == arr[pointer]) {
                count++;
                // System.out.println("count: " + String.valueOf(count));  
                if (count > len) {
                    return arr[pointer];
                }
            }
            else count = 1;
        }
        return arr[0];
    }
}
