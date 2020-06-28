"""Given a singly linked list, determine if it is a palindrome."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp_list = []
        itr = head
        while itr:
            temp_list.append(itr.val)
            itr = itr.next
        
        while itr:
            if itr.val != temp_list.pop():
                return False
            itr = itr.next
        return True

      