#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    visitedSet = set()
    while headA:
        visitedSet.add(headA.val)
        headA = headA.next
        
    while headB:
        if headB.val in visitedSet:
            return headB.val
            break
        else:
            return None
        headB = headB.next

node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(6)

nodeA = ListNode('a')
nodeB = ListNode('b')
nodeC = ListNode('c')
nodeD = ListNode('d')

node1.next = node2
node2.next = node3
node3.next = node4

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = node3

print(getIntersectionNode(node1, nodeA))