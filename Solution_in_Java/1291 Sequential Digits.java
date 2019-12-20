class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> seq = new ArrayList<>();
        int len_low = String.valueOf(low).length();
        int len_high = String.valueOf(high).length();
        int diff = len_low - 1;
        int res;
        while ( diff <= len_high  ) {
            for (int i = 1; i + diff < 10; i++){
                // System.out.println("guard: " + String.valueOf(diff + i));
                res = getSeq(i, diff);
                if (res >= low && res <= high){
                    seq.add(res);
                }
            }
            diff++;
            // System.out.println("diff++, new: " + String.valueOf(diff));
        }
        return seq;
    }
    
    public int getSeq(int start, int diff){
        int ans = start;
        for (int j = 1; j <= diff; j++){
            ans = ans*10 + j + start;
        }
        // System.out.println("here: " + String.valueOf(ans));
        return ans;
    }
}
