class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Circular:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes = []
        nodes.append(repr(cur.data))
        cur = cur.next
        while cur !=self.head:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '['+','.join(nodes)+']'

    def fibnocci(self,maxnum):
        fib = []
        first = 0
        second = 1
        final = first + second
        fib.append(first)
        fib.append(second)
        fib.append(final)
        while final <= maxnum:
            first = second
            second = final
            final = first + second
            fib.append(final)

        return fib

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        
        if self.head is not None:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next =self.head
        else:
            self.head = new_node
            new_node.next =self.head

    def remove_fibnocci(self):
        cur = self.head
        maxnum = -1234
        while True:
            if cur.data > maxnum:
                maxnum = cur.data
            
            cur = cur.next
            if cur == self.head:
                break
            
        fib = self.fibnocci(maxnum)
        cur = self.head
        temp = self.head
        prev = None
        while True:
            if cur.data in fib:
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next
            if cur.next == temp:
                break
            prev = cur
            cur = cur.next
            
        cur.next = self.head
        print(self)

    def prime(self, n):
        prime_list = [1]
        for i in range(2,n):
            c = 0
            for j in range(1,i+1):
                if i%j ==0:
                    c +=1
            if c ==2:
                prime_list.append(i)
                
        return prime_list

    def product_prime(self):
        maxnum = -1234
        cur = self.head
        while True:
            if cur.data > maxnum:
                maxnum = cur.data
            
            if cur.next == self.head:
                break
            cur = cur.next

        prime_list = self.prime(maxnum)

        cur = self.head
        prev = None
        temp = self.head
        product = 1
        
        while True:
            if cur.data in prime_list:
                product = product * cur.data
            if cur.next == temp:
                break
            cur = cur.next

        return product

    #remove every k node form list
    def remove_k_node(self, k):
        c = 1
        cur = self.head
        temp = self.head
        prev = None
        while True:
            if c == k:
                if cur != self.head:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                c = 0
            c +=1
            if cur.next == temp:
                break
            prev = cur
            cur = cur.next

        cur.next = self.head
        return self.head

    def delete_at(self, pos):
        c =0
        cur = self.head
        temp = self.head
        prev = None
        while True:
            if c == (pos-1):
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next

            c +=1
            if cur.next == temp:
                break
            prev = cur
            cur = cur.next

        cur.next = self.head

    def reverse(self):
        cur = self.head
        next = None
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            if next == self.head:
                break
            cur = next

        self.head.next = prev
        self.head = prev
         
                
if __name__ == "__main__":
    c = Circular()
    c.append(1)
    c.append(2)
    c.append(3)
    c.append(4)
    c.append(12)
    c.append(9)
    c.append(7)
    print(c)
    c.reverse()
    print(c)
        
