# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 =i= 0
        while l1:
            num1 = (l1.val * pow(10,i)) + num1
            i += 1
            l1 = l1.next

        j = 0
        while l2:
            num2 = (l2.val * pow(10,j)) + num2
            j += 1
            l2 = l2.next
        plus = num1 + num2
        new_node = ListNode(plus % 10)
        head = curr = new_node
        plus = plus//10

        while plus > 0:
            new_node = ListNode(plus % 10)
            curr.next = new_node
            curr = curr.next
            plus = plus // 10



        return head
        
