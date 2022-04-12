#header is not given , only pointer of node to be deleted will be given
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

def delete(ptr):
    if ptr is None:
        return None

    while ptr.next:
        next = ptr.next
        prev = ptr
        ptr.data , next.data = next.data, ptr.data
        ptr = ptr.next
    prev.next = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    print(ll)
    delete(ll.head.next.next.next)
    print(ll)

    
        
