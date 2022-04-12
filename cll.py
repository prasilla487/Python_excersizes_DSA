class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None;

    def __repr__(self):
        return repr(self.data)

class CLinkedList:
    def __init__(self):
        self.last = None

    def addtoempty(self, data):
        if (self.last !=None):
            return self.last

        new = Node(data)
        self.last = new

        self.last.next = self.last

    def traverse(self):
        cur = self.last
        nodes =[]
        if cur is None:
            print("emptylist")
            return
        cur = self.last.next
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next
            if cur == self.last.next:
                return '['+','.join(nodes)+']'
        
            
        
    def addlast(self, data):
        if self.last is None:
            self.addtoempty(data)

        new = Node(data)
        new.next = self.last.next
        self.last.next = new
        self.last = new

    def addbegin(self, data):
        if self.last is None:
            self.addtoempty(data)

        cur = self.last.next
        new = Node(data)
        self.last.next = new
        new.next = cur
        

    def __repr__(self):
         cur = self.last
         nodes =[]
         if cur is None:
             print("emptylist")
             return
         cur = self.last.next
         while cur:
             nodes.append(repr(cur.data))
             cur = cur.next
             if cur == self.last.next:
                 return '['+','.join(nodes)+']'

    def insert(self, index, data):
        cur = self.last.next
        if index>self.getcount():
            return print("index out of range")

        for i in range(index-1):
            cur = cur.next

        new = Node(data)
        new.next = cur.next
        cur.next = new

    def getcount(self):
        last = self.last.next
        nodes = []
        while last:
            nodes.append(repr(last.data))
            last = last.next
            if last == self.last.next:
                return len(nodes)
            
    def addafter(self,after,data):
        cur = self.last.next
        while cur and cur.data != after:
            cur = cur.next
            
        new = Node(data)
        if cur == self.last:
            new.next = cur.next
            cur.next = new
            self.last = new
        else:
            new.next = cur.next
            cur.next = new
            
    def delete(self,key):
        if self.last is None:
            return print('no elements to delete')
        cur = self.last.next
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur == self.last.next:
                return print('element not found')
        if prev is None:
            self.last.next = cur.next
        elif cur == self.last.next:
            prev.next = self.last.next
            self.last = prev
        else:
            prev.next = cur.next

    def reverse(self):
        cur = self.last.next
        temp = self.last.next
        prev = None
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        while cur != temp:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        cur.next = prev
        self.last = cur
        
        
                            
        
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes =[]
        while cur:
            nodes.append(repr(cur.data))
            cur=cur.next

        return '['+','.join(nodes)+']'

    def insert(self, data):
        new = Node(data)
        cur = self.head
        self.head = new
        self.head.next = cur

    def getcount(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return (len(nodes))


    def search(self, key):
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        if cur is not None:
            print("found")
        else:
            print("not found")

    def append(self, data):
        new = Node(data)
        cur = self.head
        while cur:
            prev = cur
            cur = cur.next
        if prev is None:
            self.head = new
        else:
            prev.next = new

    def setnode(self, index,data):
        cur = self.head
        new = Node(data)
        if index > self.getcount():
            return print("Incorrect index")
        
        else:
            for i in range(1,(index+1)):
                prev = cur
                cur = cur.next
            prev.next = new
            prev.next.next = cur
            
    def delete(self, data):
        if self.head is None:
            return print("list is empty")
        cur = self.head
        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if cur:
            self.head = cur.next
        elif prev and cur is None:
            return print("element not found")
        else:
            prev.next = cur.next

    
                
        
            

    
if __name__=="__main__":
    newNode = None
    head1 = Node() 
    head1.data = 10
    head2 = Node() 
    head2.data = 3
    newNode = Node() 
    newNode.data = 6
    head2.next = newNode 
    newNode = Node() 
    newNode.data = 9
    head2.next.next = newNode 
    newNode = Node() 
    newNode.data = 15
    head1.next = newNode 
    head2.next.next.next = newNode 
    newNode = Node() 
    newNode.data = 30
    head1.next.next = newNode 
    head1.next.next.next = None

