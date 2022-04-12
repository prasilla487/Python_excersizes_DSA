#get nth node from end
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

    def getNthNode(self, n):
        size = self.size()
        n = size -n
        count = 0
        cur = self.head
        flag = 0
        while cur:
            if count == n:
                flag = 1
                break
            count +=1
            cur = cur.next

        if flag:
            return cur
        else:
            return -1

    #to get nth node
    def method2(self, n):
        main_ptr = ref_ptr = self.head
        count = 0
        while count < n:
            if ref_ptr is None:
                return -1

            ref_ptr = ref_ptr.next
            count +=1

        while ref_ptr is not None:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr
        


if __name__ == '__main__':
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
    print(ll.method2(5))
