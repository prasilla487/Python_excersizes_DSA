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

    def push(self, data):
        new = Node(data)
        cur = self.head
        if cur is None:
            self.head = new
            return

        if data == 0:
            new.next = self.head
            self.head = new
        elif data == 1:
            prev = None
            while cur and cur.data == 0:
                prev = cur
                cur = cur.next
            if prev is not None:
                new.next = prev.next
                prev.next = new
            elif self.head is not None and prev is None:
                new.next = self.head
                self.head = new
            else:
                self.head = new
        else:
            while cur.next:
                cur = cur.next

            cur.next = new
                
                

if __name__ == "__main__":
    t = int(input('no of test cases'))
    a = [2,0,1,0,2,1, 2, 0,0,2,1,2,0,1,0]
    ll = LinkedList()
    for i in a:
        ll.push(i)
    print(ll)
    for i in range(t):
        n = int(input('no of queries'))
        ar = input('enter query and values')
        ar = [int(e) for e in ar.split()]
        ll = LinkedList()
        for val in ar:
            ll.push(val)
        print(ll)
