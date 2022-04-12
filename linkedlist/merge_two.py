#merge two linkedlists in place and return head of merged list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(nodes) + ']'

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        if cur is None:
            self.head = new_node
            return

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count +=1
            cur = cur.next

        return count

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.data < h2.data:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2
        
                    
def printList(head):
    while head:
        print(head.data)
        head = head.next
     

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    ll.append(40)
    print(ll)
    l = LinkedList()
    l.append(2)
    l.append(3)
    l.append(6)
    l.append(8)
    l.append(20)
    mh = ll.merge(l.head,ll.head)
    printList(mh)

