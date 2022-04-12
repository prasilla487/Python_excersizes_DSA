# linked list of n nodes and each contains a seperate linked list, convert to flatten and sort

class Node:
    def __init__(self, data, right=None, down=None):
        self.data = data
        self.right = right
        self.down = down

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            cur2 = cur.down
            while cur2:
                nodes.append(repr(cur2.data))
                cur2 = cur2.down

            nodes.append(repr(cur.data))
            cur = cur.right

        return '[' + ','.join(nodes) + ']'



    
if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(5)
    ll.head.down = Node(7)
    ll.head.down.down = Node(8)
    ll.head.right = Node(10)
    ll.head.right.down = Node(20)
    ll.head.right.right = Node(19)
    ll.head.right.right.down = Node(22)
    ll.head.right.right.down.down = Node(50)
    ll.head.right.right.right = Node(28)
    ll.head.right.right.right.down = Node(35)
    ll.head.right.right.right.down.down = Node(40)
    print(ll)
                
