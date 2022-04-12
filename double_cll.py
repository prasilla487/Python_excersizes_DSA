class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)

class DoubleCircular:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        cur = self.head
        while True:
            nodes.append(repr(cur.data))
            if cur.next == self.head:
                break
            cur = cur.next

        return '['+','.join(nodes)+']'

    def size(self):
        c = 0
        cur = self.head
        while True:
            c+=1
            if cur.next == self.head:
                break
            cur = cur.next

        return c
            

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        cur = self.head
        
        while True:
            if cur.next == self.head:
                break
            cur = cur.next

        self.head.prev = new_node
        cur.next = new_node
        new_node.prev = cur
        new_node.next = self.head

    def insert_at(self, pos, data):
        c = 1
        new_node = Node(data)
        cur = self.head
        temp = self.head
        status = True
        while True:
            if c == pos:
                if cur == self.head:
                    new_node.next = cur
                    new_node.prev = cur.prev
                    cur.prev = new_node
                    self.head = new_node

                else:
                    new_node.next = cur.next
                    new_node.prev = cur
                    cur.next = new_node
                status = False
            c +=1
            if cur.next == temp:
                break
            cur = cur.next

        cur.next = self.head
        if status:
            new_node.next = cur.next
            new_node.prev = cur
            cur.next = new_node
            self.head.prev = new_node

    def delete_at(self, pos):
        c = 0
        cur = self.head
        temp = self.head
        prev = None
        while True:
            if c==(pos-1):
                if cur == self.head:
                    cur.next.prev = cur.prev
                    self.head = cur.next
                else:
                    prev.next = cur.next
                    cur.next.prev = prev

            c+=1
            prev = cur
            if cur.next == temp:
                break
            
            cur = cur.next
            
        cur.next = self.head
        self.head.prev = cur

    def bubblesort(self):
        temp = self.head
        cur = self.head
        end = cur
        while end:
            cur = self.head
            while cur.next != temp:
                next = cur.next
                if cur.data >next.data:
                    cur.data, next.data = next.data, cur.data
                cur = cur.next
            if end.next == temp:
                break
            end = end.next

    #not working
    def delete_duplicate(self):
        cur = self.head
        prev = []
        head = DoubleCircular()
        temp =self.head
        while cur:
            next = cur.next
            if cur.data == next.data:
                print("in")
                while (cur and cur.next) and cur.data == cur.next.data:
                    print(cur)
                    cur = cur.next
                
                cur = cur.next
                prev_next = cur
                print("out loop {0}".format(cur))
            else:
                prev.append(cur.data)
                cur = cur.next
                
            if cur == temp:
                break
        for i in prev:
            head.append(i)

        return head
            


if __name__=="__main__":
    d = DoubleCircular()
    d.append(5)
    d.append(2)
    d.append(1)
    d.append(4)
    d.append(3)
    d.append(2)
    d.append(3)
    d.append(1)
    print(d)
    d.bubblesort()
    d.delete_duplicate()
    print(d)
