# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            if list1 is not None: return list1
            if list2 is not None: return list2
            return None
        
        leftCurr = list1
        rightCurr = list2

        head = None
        if leftCurr.val <= rightCurr.val:
            head = leftCurr
            leftCurr = leftCurr.next
        else:
            head = rightCurr
            rightCurr = rightCurr.next

        realHead = head

        while leftCurr is not None and rightCurr is not None:
            if leftCurr.val <= rightCurr.val:
                head.next = leftCurr
                leftCurr = leftCurr.next
            else:
                head.next = rightCurr
                rightCurr = rightCurr.next
            head = head.next
        
        if leftCurr is not None:
            head.next = leftCurr
        else:
            head.next = rightCurr

        return realHead
        


        