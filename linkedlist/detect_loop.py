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
        d = Node(data)
        cur = self.head
        if cur is None:
            self.head = d
            return

        while cur.next:
            cur = cur.next

        cur.next = d


    def detect_loop(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print('slow is {0}, fast is {1}'.format(slow, fast))

            if slow == fast:
                print('loop detected')
                self.remove_loop(slow)
                return 1

    def remove_loop(self, slow):
        ptr1 = self.head
        while ptr1:
            ptr2 = slow
            while ptr2.next != slow and ptr2.next != ptr1:
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None

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
    print(ll)
    ll.head.next.next.next.next = ll.head.next.next
    ll.detect_loop()
    print(ll)

