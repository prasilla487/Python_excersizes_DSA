class Node:

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

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

        return '[' + ','.join(nodes) + ']'

    def append(self, data):
        cur = self.head
        if cur is None:
            node = Node(data)
            self.head = node
            node.prev = self.head
            return
            
        while cur:
            prev_node = cur
            cur = cur.next

        node = Node(data)
        prev_node.next = node
        node.prev = prev_node
        node.next = None

    def iter(self):
        cur = self.head
        while cur:
            value = cur.data
            cur = cur.next
            yield value

    def print_forward(self):
        for node in self.iter():
            print(node)

    def reverse(self):
        cur = self.head
        while cur:
            next = cur.next
            prev = cur.prev
            cur.next = prev
            cur.prev = next
            cur = cur.next

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


    def bubble_link(self):
        end = None
        while end != self.head:
            cur = self.head
            p = self.head
            
            while cur.next != end:
                print("cur is {0}, cur_next is {1}".format(cur, cur.next))
                next = cur.next
                prev = cur.prev
                if cur.data > next.data:
                   print("in")
                   cur.prev = next
                   print("cur.prev {0}".format(cur.prev))
                   cur.next = next.next
                   print("cur.next {0}".format(cur.next))
                   if prev != None:
                       next.prev = prev
                       print("next.prev {0}".format(next.prev))
                       prev.next = next
                       print("prev.next {0}".format(prev.next))
                   if next.next != None:
                       next.next.prev = cur
                   next.next = cur
                   print("next.next {0}".format(next.next))
                   
                   if self.head == cur:
                       self.head = next
                       print("self.head {0}".format(self.head))
                else:
                    p = p.next

                print(self)
                cur = p            
            
                
            end = cur

    def removeduplicate(self):
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next

            else:
                cur = cur.next
                
    def merge(self, l):
        result = LinkedList()
        first = self.head
        second = l.head

        if first.data <second.data:
            result.head = Node(first.data)
            first = first.next
        else:
            result.head = Node(second.data)
            second = second.next

        while first and second:
            if first.data < second.data:
                result.append(first.data)
                first = first.next
            else:
                result.append(second.data)
                second = second.next

        while first:
            result.append(first.data)
            first = first.next

        while second:
            result.append(second.data)
            second = second.next

        print(result)

    def sortedinsert(self, data):
        new_node = Node(data)
        cur = self.head
        while cur and cur.data <data:                                                                                                                                                                                                                           
            cur = cur.next

        new_node.prev = cur
        new_node.next = cur.next
        cur.next = new_node

        
if __name__ == "__main__":
    dll = LinkedList()
    dll.append(4)
    dll.append(2)
    dll.append(3)
    dll.append(1)
    dll.append(1)
    dll.append(2)
    
    dll.bubblesort()
    print(dll)
    dll.removeduplicate()

    d = LinkedList()
    d.append(10)
    d.append(5)
    d.append(6)
    d.append(9)
    d.append(8)
    d.append(7)
    d.bubblesort()
    print(d)
    d.sortedinsert(5)
    print(d)
    

    
    
    
