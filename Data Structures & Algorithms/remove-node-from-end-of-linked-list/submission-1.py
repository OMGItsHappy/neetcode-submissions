# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            length += 1

        ptr = head
        curr = 1
        if length - n == 0: return ptr.next
        while ptr.next and curr < length - n:
            ptr = ptr.next
            curr += 1

        if n == 1:
            if length == 1: return None
            ptr.next = None
        else:
            ptr.next = ptr.next.next

        return head