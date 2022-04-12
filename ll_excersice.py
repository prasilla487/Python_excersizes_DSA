class Node:
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(repr(cur))
            cur = cur.next_node
        return '['+','.join(nodes) + ']'

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next_node

        prev.next_node = Node(data)

    def get_size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next_node
        return count

    def find_item(self, key):
        cur = self.head
        while cur and cur.data!=key:
            cur = cur.next_node
        if cur:
            return True
        else:
            return False

    def __getitem__(self, index):

        cur = self.get_size()-1
        if index > cur:
            return 'Index out of range'
        cur = self.head
        for i in range(index+1):
            data = cur.data
            cur = cur.next_node
        return data

    def __setitem__(self, index ,data):
        cur = self.head
        if index > (self.get_size())-1:
            raise Exception("Index out of range")
        if index==0:
            self.head = Node(data)
            self.head.next_node = cur
            return
        for i in range(index-1):
            cur = cur.next_node
        temp = cur.next_node
        cur.next_node = Node(data)
        cur.next_node.next_node = temp

    def delete_first(self):
        cur = self.head
        if cur is not None:
            self.head = cur.next_node

    def delete_last(self):
        cur = self.head
        prev = None
        for i in range(self.get_size()-1):
            prev = cur
            cur = cur.next_node
        if prev is None:
            self.head = None
        else:
            prev.next_node = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
