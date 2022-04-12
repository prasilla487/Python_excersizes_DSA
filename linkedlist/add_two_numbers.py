#given two numbers represented by linked list find the result sum
#number is represented in reverse order like 123 ll: 3 -> 2-> 1
#op should be in reverse order

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

    #method1 here least significant digit is first node and most significant is last node
    def addTwo(self, l):
        cur1 = self.head
        cur2 = l.head
        div  = 0
        new_ll = LinkedList()
        while True:
            if cur1 is None and cur2 is None:
                return new_ll.head
            fdata = 0 if cur1 is None else cur1.data
            sdata = 0 if cur2 is None else cur2.data
            cur_sum = fdata + sdata + div
            div = cur_sum //10
            print('div is {0}'.format(div))
            rem = cur_sum % 10
            print('rem is {0}'.format(rem))
            new_ll.append(Node(rem))
            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next

        if div > 0:
            new_ll.append(Node(div))

        return new_ll.head

    def push(self, k, data):
        new_node = Node(data)
        cur = self.head
        if cur is None:
            self.head = new_node
            return
        count = 0
        while cur and count < k:
            cur = cur.next
            count +=1

        if cur == self.head:
            new_node.next = self.head
            self.head = new_node
            return


    def addSameSize(self, h1, h2, carry):

        if h1 is None:
            return 0


        carry = self.addSameSize(h1.next, h2.next, carry)

        cur_sum = h1.data + h2.data + carry
        carry = cur_sum // 10

        cur_sum = cur_sum % 10
        self.push(0,cur_sum)

        return carry


    #method2 here most significant digit is the first node and least significant digit is last node
    def addNumbers(self, h1, h2):
        if h1 is None:
            self.append(Node(h2))
            return
        
        if h2 is None:
            self.append(Node(h1))
            return

        size1 = size(h1)
        size2 = size(h2)

        carry = 0
        if size1 == size2:
            carry = self.addSameSize(h1, h2,0)
            if carry >0:
                self.push(0,carry)
        else:
            diff = abs(size1 - size2)

            if size1 < size2:
                h1, h2 = h2, h1

            count = 0
            cur = h1
            while h1 and count < diff:
                h1 = h1.next
                count +=1
            
            carry = self.addSameSize(h1, h2, 0)
            count = 0
            while cur and count < diff:
                print(cur, carry)
                cur_sum = cur.data + carry
                carry = cur_sum // 10
                cur_sum = cur_sum % 10
                self.push(0, cur_sum)
                count +=1
                cur = cur.next

            if carry > 0:
                self.push(0, carry)
        
            


def printList(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next

    print(nodes)

def size(head):
    count = 0
    cur = head
    while cur:
        count +=1
        cur = cur.next
    
    return count

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(9)
    ll.append(9)
    ll.append(9)
    ll.append(4)
    ll.append(6)
    l = LinkedList()
    l.append(1)
    l.append(8)
    #l.append(2)
    result = LinkedList()
    result.addNumbers(ll.head, l.head)
    print(result)
    
            
            
            
