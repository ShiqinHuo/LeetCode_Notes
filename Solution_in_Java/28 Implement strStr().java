class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.equals("")) return 0;
        int L = needle.length();
        for(int i=0; i<=haystack.length()-L; i++) 
            if(haystack.substring(i,i+L).equals(needle)) return i;
        return -1;
    }
}
