#pairwise swap the elements of linkedlist ex: l [1,2,3,4] op: [2,1,4,3]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        cur = self.head
        if cur is None:
            self.head = new
            return

        while cur.next:
            cur = cur.next

        cur.next = new


    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(nodes) + ']'

    def swap(self, h):
        cur = self.head
        while cur is not None and cur.next is not None:
            cur.data , cur.next.data = cur.next.data, cur.data
            cur = cur.next.next

        return h

def printlist(head):
    cur = head
    nodes = []
    while cur:
        nodes.append((cur.data))
        cur = cur.next

    print(nodes)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll)
    h = ll.swap(ll.head)
    printlist(h)
