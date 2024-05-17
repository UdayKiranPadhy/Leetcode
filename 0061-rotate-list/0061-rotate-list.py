# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        N = getLength(head)
        if N==0:
            return head
        k = k%N
        if k==0:
            return head
        left = N - k
        curr = head
        
        for i in range(left-1):
            curr = curr.next
        newhead = curr.next
        curr.next = None
        curr = newhead
        while curr.next:
            curr = curr.next
        curr.next = head
        return newhead