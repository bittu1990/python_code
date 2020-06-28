"""Given a sorted linked list,
delete all duplicates such that each element appear only once."""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        preptr, ptr = head, head
        while ptr.next:
            ptr = ptr.next
            if preptr.val != ptr.val:
                preptr.next = ptr
                preptr = ptr
            
        preptr.next = None
        return head

if __name__ == '__main__':
    ll = Solution()
    pp = ListNode(2)
    ll.deleteDuplicates(pp)
    print(ll)