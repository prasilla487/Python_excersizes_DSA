#rotate the list by k nodes in counter-clock wise direction
# l = 1,2,3,4,5 k=2 op: 3,4,5,1,2

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


    def rotate(self,k):
        count = 0
        cur = self.head
        while cur:
            if count == k:
                break
            prev = cur
            cur = cur.next
            count +=1

        
        while cur.next:
            cur = cur.next
        cur.next = self.head
        self.head = prev.next
        prev.next = None



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    print(ll)
    ll.rotate(4)
    print(ll)
