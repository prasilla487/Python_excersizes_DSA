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
        cur = self.head
        new_node = Node(data)
        if cur is None:
            self.head = new_node
            return
        
        while cur.next:
            cur = cur.next
        
        cur.next = new_node

    def __repr__(self):
        cur = self.head

        nodes = []
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(nodes) + ']'

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next

        return count

    def getMiddle(self):
        size = self.size()
        middle = size //2
        count = 0
        cur = self.head
        if cur is None:
            return print('empty list')

        while cur:
            if count == middle:
                print('middle element is {0}'.format(cur.data))

            count +=1
            cur = cur.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(ll)
    ll.getMiddle()
            
