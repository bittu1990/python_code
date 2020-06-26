class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' ===> '
            itr = itr.next
        print(llstr)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count


    def insertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)


    def insertAt(self, pos, data):
        if pos < 0  or pos > self.getLength():
            raise Exception ("Invalid Index")

        if pos == 0:
            self.insertAtBegining(data)
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == pos - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            cnt += 1

    def removeAt(self, pos):
        if pos<0 or pos>= self.getLength():
            raise Exception("Invalid Index")

        if pos == 0:
            self.head = self.head.next
            return

        cnt = 0
        itr = self.head
        while itr:
            if cnt == pos - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            cnt += 1
    
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)
    
    
    def insetValueAfter(self, data_after, data):
        cnt = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            cnt += 1

    def removeByValue(self, item):
        cnt = 0
        itr = self.head

        while itr:
            if itr.data == item:
                self.removeAt(cnt)
            
            itr = itr.next
            cnt +=1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegining(5)
    ll.insertAtBegining(11)
    ll.insertAtEnd(34)
    ll.printing()
    ll.insertAt(1,99)
    ll.printing()
    ll.removeAt(2)
    ll.printing()
    ll.insertValues(['banana', 'mango', 'grapes', 'orange'])
    ll.printing()
    ll.insetValueAfter('mango', 'apple')
    ll.printing()
    ll.removeByValue('orange')
    ll.printing()
    ll.removeByValue('figs')
    ll.removeByValue('banana')
    ll.removeByValue('mango')
    ll.removeByValue('apple')
    ll.removeByValue('grapes')
    ll.printing()