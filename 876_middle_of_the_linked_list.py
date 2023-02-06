#https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=level-1
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = h2 = head
        while h2 and (h2:= h2.next):
            if h2: h2 = h2.next;h1= h1.next
        return h1