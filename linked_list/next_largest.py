#Definition for singly-linked list.
"""
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def nextLargerNodes(head: ListNode):
        
    result = []
    start = head
    counter = head.next

    while start.next:
        
        temp =[]
        while counter.next:
            
            print(counter.val)
            if counter.val > start.val:
                temp.append(counter.val)
                
            else:
                temp.append(0)  
            
            
            counter = counter.next
            print(counter.val)
            result.append(max(temp))

        start = start.next
    return result

node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(5)
node4 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4

print(nextLargerNodes(node1))
