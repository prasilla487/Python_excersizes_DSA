class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
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
        
        return '['+','.join(nodes)+']'

    def append(self, data):
        cur = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        while cur.next:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur
    
    def begin_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        self.head = new_node
        new_node.next = cur
        cur.prev = new_node

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        
        return count

    def insert_at(self, data, pos):
        new_node = Node(data)

        if pos > self.size():
            return print('position not found')
        
        cur = self.head
        for i in range(0, self.size()):
            if i == (pos-1):
                break
            cur = cur.next

        new_node.next = cur.next
        new_node.prev = cur
        cur.next = new_node

    def delete_at(self, pos):
        count = self.size()
        if pos > count:
            return print("No element found in position")
        
        cur = self.head
        for i in range(0, count):
            if i == (pos-1):
                break
            cur = cur.next
        
        if cur == self.head:
            self.head = cur.next
            self.head.prev = None
        if cur.next != None:
            cur.next.prev = cur.prev
        if cur.prev != None:
            cur.prev.next = cur.next

    #delete all the occurences of given key
    def deletekey(self,key):
        cur = self.head
        while cur:
            if cur.data == key:
                self.deletenode(cur)
            
            cur = cur.next
    
    #delete the given node
    def deletenode(self, del_):
        if del_ is self.head:
            self.head = del_.next
            del_.next.prev = None

        if del_.next != None:
            del_.next.prev = del_.prev
        
        if del_.prev != None:
            del_.prev.next = del_.next
        
        return self.head

    #delete all nodes less than the given value
    def deletesmallervalue(self, val):
        cur = self.head
        while cur:
            if cur.data <= val:
                self.deletenode(cur)
            
            cur = cur.next

    #delete all nodes greateer than the given value
    def deletegreatervalue(self, val):
        cur = self.head
        while cur:
            if cur.data >= val:
                self.deletenode(cur)
            
            cur = cur.next
    
    #delete all nodes divisible by k
    def delete_divisible(self, k):
        cur = self.head
        while cur:
            if (cur.data)%k == 0:
                self.deletenode(cur)
            
            cur = cur.next

if __name__=="__main__":
    l = LinkedList()
    l.append(4)
    l.append(5)
    l.begin_insert(1)
    l.begin_insert(8)
    l.begin_insert(2)
    l.append(6)
    l.append(3)
    print(l)
    l.delete_divisible(2)
    print(l)
