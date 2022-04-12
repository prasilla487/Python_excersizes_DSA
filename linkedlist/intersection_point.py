class Node:
    def __init__(self, data, next=None):
        self.data = data
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

        return '[' + ','.join(nodes) + ']'

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        if cur is None:
            self.head = new_node
            return

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count +=1
            cur = cur.next

        return count


    def findIntersection(self, l):
        count2 = l.size()
        count1 = self.size()
        diff = count1 - count2
        count = 0
        node1 = self.head
        while count < diff:
            node1 = node1.next
            count +=1

        cur1 = node1
        cur2 = l.head
        while cur1 is not None and cur2 is not None:
            if cur1 == cur2:
                print("Intersection is at node {0}".format(cur1.data))
                return
            cur1 = cur1.next
            cur2 = cur2.next

            

if __name__ == '__main__':
    l1 = LinkedList()
    l1.head = Node(3)
    l1.head.next = Node(6)
    l1.head.next.next = Node(9)
    l1.head.next.next.next = Node(10)
    l1.head.next.next.next.next = Node(30)
    l1.head.next.next.next.next.next = Node(5)
    l2 = LinkedList()
    l2.head = Node(15)
    l2.head.next = l1.head.next.next.next
    print(l1)
    print(l2)
    l1.findIntersection(l2)
    
