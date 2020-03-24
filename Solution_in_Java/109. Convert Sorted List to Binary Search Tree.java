class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        return helper(head, null);
    }
    
    /**
        Find the middle, root is the middle.
        left subtree is left part of middle.
        right subtree is right part of middle.
    */
    public TreeNode helper(ListNode head, ListNode tail) {
        ListNode slow = head;
        ListNode fast = head;
        if (head==tail) return null;
        
        while (fast!=tail && fast.next!=tail) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        TreeNode midNode = new TreeNode(slow.val);
        midNode.left = helper(head, slow);
        midNode.right = helper(slow.next, tail);
        return midNode;
    }
}
