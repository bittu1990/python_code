#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        itr = head
        while itr:
            nextnode = itr.next
            itr.next = temp
            temp = itr
            itr = nextnode
            
        return temp