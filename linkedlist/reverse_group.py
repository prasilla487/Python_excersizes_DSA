#reverse every k group of elements in linkedlist
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
        new_node = Node(data)
        cur = self.head
        if cur is None:
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

        return '[' + ','.join(nodes) + ']'

    def reverse_group(self, head,k):
        count = 0
        cur = head
        prev = None
        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count +=1

        if next is not None:
            head.next = self.reverse_group(next, k)

        return prev
        


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
    ll.append(9)
    ll.append(10)
    ll.append(11)
    ll.append(12)
    print(ll)
    ll.head = ll.reverse_group(ll.head,3)
    print(ll)
