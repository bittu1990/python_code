""" Find the middle of the Linked List given the head node
3->4->5 : 4
3->4->5->6 : 5  """

class LinkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

def getMiddle(head):
    fastRunner = head
    slowRunner = head
    tick = False
    while fastRunner:
        fastRunner = fastRunner.nextNode
        if tick:
            slowRunner = slowRunner.nextNode
        tick = not tick
    
    return slowRunner.value

node1 = LinkedListNode(3)
node2 = LinkedListNode(4)
node3 = LinkedListNode(5)
node4 = LinkedListNode(6)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

print(getMiddle(node1))