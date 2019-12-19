/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int ans = head.val;
        ListNode current = head;
        while (current.next != null){
            current = current.next;
            ans = ans*2 + current.val;
        }
        return ans;
    }
}
