# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        can_reverse = True

        while can_reverse:
            curr = prev.next
            for _ in range(k-1):
                move = curr.next
                curr.next = move.next
                move.next = prev.next
                prev.next = move
                
            prev = curr

            temp = prev
            for _ in range(k):
                temp = temp.next
                if temp is None:
                    can_reverse = False
                    break
                
        return dummy.next