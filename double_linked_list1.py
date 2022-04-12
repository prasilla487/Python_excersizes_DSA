class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)

class DoubleLinked:
    def __init__(self):
        self.head = None

    def append(self, data):
        cur = self.head
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        while cur.next:
            cur = cur.next
        
        cur.next = new_node
        new_node.prev = cur

    def __repr__(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next
        
        return '['+','.join(nodes)+']'

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        
        return count

    def fibnocci(self, n):
        fib = []
        first = 0
        second = 1
        final = first + second
        fib.append(first)
        fib.append(second)
        fib.append(final)
        while final <= n:
            first = second
            second = final
            final = first + second
            fib.append(final)
        
        return fib

    def delete_fibnocci(self):
        cur = self.head
        maxnum = -12345

        while cur:
            if maxnum < cur.data:
                maxnum = cur.data
            cur = cur.next
        
        fib = self.fibnocci(maxnum)
        cur = self.head
        while cur:
            next = cur.next
            if cur.data in fib:
                next.prev = cur
                if self.head !=cur:
                    prev.next = next
                else:
                    self.head = next
                    next.prev = None
            
            prev = cur
            cur = cur.next

        print(self)


    #swap kth node from begining with kth node from end
    def replace_k_node(self, k):
        count = 1
        cur = self.head
        
        while cur:
            if count == k:
                temp = cur
            if count == (self.size()-k)+1:
                cur.data, temp.data = temp.data, cur.data
                break
                
            count +=1
            cur = cur.next

    def deleteNode(self, cur):
        prev = cur.prev
        next = cur.next

        if cur !=self.head:
            if cur.next !=None:
                prev.next = next
                next.prev = prev
        else:
            self.head = next
            self.head.prev = None

    def bubblesort(self):
        end = None
        while end != self.head:
            cur = self.head
            prev = self.head
            while cur.next != end:
                next = cur.next
                if cur.data > next.data:
                    cur.data, next.data = next.data, cur.data
                
                cur = cur.next

            end = cur
        
        return self.head

    def remove_common(self, l):
        self.bubblesort()
        
        l.bubblesort()
        result = DoubleLinked()
        cur1 = self.head
        cur2 = l.head
        a = cur1
        b = cur2
        while cur1 != None and cur2 !=None:
            cur2 = l.head
            count =0
            while cur2 != None:
                if cur1.data == cur2.data:
                    count = 1
                cur2 = cur2.next
            
            if count == 0:
                result.append(cur1.data)
            

            cur1 = cur1.next

        while cur1:
            result.append(cur1.data)
            cur1 = cur1.next
        
        while cur2:
            result.append(cur2.data)
            cur2 =cur2.next


        print(result)

    #replace all even nodes with the elements of given array
    def replace_even(self, ar):
        cur = self.head
        i =0
        c = 1
        while cur:
            if c%2 == 0:
                cur.data = ar[i]
                i +=1

            c+=1
            cur = cur.next

        print(self)

    def build_greater(self, l):
        result = DoubleLinked()
        cur1 = self.head
        cur2 = l.head

        while cur1 and cur2:
            if cur1.data > cur2.data:
                result.append(cur1.data)
            else:
                result.append(cur2.data)

            cur1 = cur1.next
            cur2 = cur2.next

        print(result)

    def swap_k_node(self, k):
        first = self.head
        while first:
            last = first
            first = first.next

        first = self.head
        c =1
 
        while first and c !=k:
            c+=1
            first = first.next
            last = last.prev

        if first is None and last is None:
            return print("Size is exceeded")
        else:
            first.data, last.data = last.data, first.data

    def size(self):
        cur = self.head
        c = 0
        while cur:
            c +=1
            cur = cur.next
        return c

    def reverse(self):
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev

        if temp is not None: 
            self.head = temp.prev

    def rotate_n_nodes(self, n):
        size = self.size()
        if n > 0 and n < size:
            cur = self.head
            c = 1
            while cur:
                next = cur.next
                if c == n:
                    break
                c+=1
                cur = cur.next
            
            temp = cur
            while temp.next:
                temp = temp.next
            
            temp.next = self.head
            cur.next = None
            next.prev = None
            self.head = next
            
        
            
        

if __name__ == "__main__":
    l = DoubleLinked()
    l.append(13)
    l.append(7)
    l.append(8)
    l.append(16)
    l.append(14)
    l.append(12)
    print(l)
    l.rotate_n_nodes(3)
    print(l)

    
