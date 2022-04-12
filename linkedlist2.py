class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    
    def __init__(self):
        self.head = None

    def size(self):
        c = 0
        cur = self.head
        while cur:
            c +=1
            cur = cur.next
        
        return c
    
    def append(self, data):
        cur = self.head
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 
        
        while cur.next:
            cur = cur.next
        
        cur.next = new_node

    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next
        
        return '['+','.join(nodes)+']'

    def swaplink(self):
        end = None
        while end != self.head:
            cur = self.head
            prev = self.head
            
            while cur.next != end:
                print(cur.next)
                next = cur.next
                if cur.data > next.data:
                    cur.next = next.next
                    next.next = cur
                    if self.head != cur:
                        prev.next = next
                    else:
                        self.head = next

                    cur,next = next, cur
                prev = cur
                cur = cur.next
            
            end = cur

    def fibnocii(self,num):
        fib = []
        first = 0
        second = 1
        final = first + second
        fib.append(first)
        fib.append(second)
        fib.append(final)
        first = second
        second = final
        final = first + second
        fib.append(final)
        while final < num:
            first = second
            second = final
            final = first + second
            fib.append(final)
        print(fib)
        return fib
            

    #delete nodes which are fibnocii numbers
    def delete_fib(self):
        maxnum = -234
        cur = self.head
        while cur:
            if cur.data > maxnum:
                maxnum = cur.data
            cur = cur.next
        
        fib = self.fibnocii(maxnum)
    
        cur = self.head
        prev = None
        while cur:
            if cur.data in fib:
                if cur !=self.head:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                prev, cur = cur, prev
            
            prev = cur
            cur = cur.next
        
    #move n nodes from last to front of list   
    def move_to_front(self, m):
        n = (self.size()-m) +1
        cur = self.head
        cur2 = self.head
        c = 1
        while cur:
            if c==n:
                while cur!=None:
                    temp = cur.next
                    cur.next = self.head
                    self.head = cur
                    cur = cur.next
            c +=1
            cur = cur.next

    #use hashing technique
    def detectloop(self):
        s = set()
        cur = self.head
        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next

    #using floyds cycle detecting algorithm
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.remove_loop(slow)
                return 1

        return 0

    def remove_loop(self, loopnode):
        ptr1 = self.head
        while(1):
            ptr2 = loopnode
            while ptr2.next != loopnode and ptr2.next != ptr1:
                ptr2 =  ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None    


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    

if __name__ == "__main__":
    llist = LinkedList() 
    llist.append(10) 
    llist.append(4) 
    llist.append(15) 
    llist.append(20) 
    llist.append(50)
    #llist.print_list()
    llist.head.next.next.next.next.next = llist.head.next.next
    llist.detect_loop()
    llist.print_list()
    
    

