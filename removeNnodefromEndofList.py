https://neetcode.io/problems/remove-node-from-end-of-linked-list/history?list=neetcode150&submissionIndex=0
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        left,right = dummy,head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next