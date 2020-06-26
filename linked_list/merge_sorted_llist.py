
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node = node.next
        result = ListNode(-1)
        temp = result
        while heap:
            k = heapq.heappop(heap)
            temp.next = ListNode(k)
            temp = temp.next
        temp.next = None
        return result.next