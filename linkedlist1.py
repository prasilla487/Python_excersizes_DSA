class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '['+','.join(nodes)+']'

    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def bubblesort(self):
        end = None
        while end != self.head:
            cur = self.head
            while cur.next != end:
                next = cur.next
                if cur.data > next.data:
                    cur.data, next.data = next.data, cur.data

                cur = cur.next
            end = cur

    def removeduplicates(self):
        cur = self.head
        while cur.next:
            print("cur is {0} cur.next is {1}".format(cur, cur.next))
            if cur.data == cur.next.data:
                new = cur.next.next
                cur.next= None
                cur.next = new
            else:
                cur = cur.next
                
        print(self)
        
    def merge(self, l):
        new_link = Linkedlist()
        first = self.head
        second = l.head
        if first.data > second.data:
            new_link.head = Node(second)
            second = second.next
        else:
            new_link.head = Node(first)
            first = first.next

        while first.next !=None and second.next !=None:
            if first.data > second.data:
                new_link.append(second.data)
                second = second.next
            else:
                new_link.append(first.data)
                first = first.next

        while first != None:
            new_link.append(first.data)
            first = first.next

        while second != None:
            new_link.append(second.data)
            second = second.next
        print(new_link)
                
        new_link.removeduplicates()



if __name__ == "__main__":
    l3 = Linkedlist()
    l3.append(1)
    l3.append(1)
    l3.append(2)
    l3.append(4)
    l3.append(5)
    l3.append(7)
    l3.append(9)
    l3.bubblesort()
    print(l3)
    l3.removeduplicates()
