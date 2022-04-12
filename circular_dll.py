class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = None
        self.next = None

    def repr(self):
        return repr(self.data)

class Circular:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(repr(cur.data))
            if cur.next == self.head:
                break
            cur = cur.next
        
        return '['+','.join(nodes)+']'
    
    def append(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return self.head
        
        cur = self.head
        while cur:
            next = cur.next
            if next == self.head:
                break
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur
        new_node.next = self.head
        self.head.prev = new_node

    def reverse(self):
        cur = self.head
        while cur:
            temp = cur.prev
            next = cur.next
            cur.prev = cur.next
            cur.next = temp
            if next == self.head:
                break
            cur = cur.prev

        if temp is not None:
            self.head = temp.prev

    

if __name__ == "__main__":
    l = Circular()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    print(l)
    l.reverse()
    print(l)