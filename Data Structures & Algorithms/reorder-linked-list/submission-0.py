class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
            
        fast = slow = first = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        middle = slow
        second = middle.next
        middle.next = None  # Crucial: cut the list into two halves

        # Reverse the second half
        prev = None
        curr = second
        while curr:
            ne = curr.next
            curr.next = prev
            prev = curr
            curr = ne
        
        # Merge the two halves
        second = prev
        while second:
            f_next = first.next
            s_next = second.next

            first.next = second
            first = f_next

            second.next = first
            second = s_next

        # Change 'return head' to just 'return' or remove it
        return
