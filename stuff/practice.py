class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    visited_set = set()
    while headA:
        visited_set.add(headA.val)
        headA = headA.next
    #print(visited_set)
    while headB:
        #print(headB.val)
        if headB.val in visited_set:
            return headB.val
            break
        
        headB = headB.next
    return None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

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
#nodeD.next = node2

print(getIntersectionNode(node1, nodeA))
