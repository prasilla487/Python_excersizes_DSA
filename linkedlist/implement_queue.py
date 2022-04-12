#do queries , if input contains 1 x need to push x into the queue, if 2 pop element
# inp : 1 2 1 3 2  op: 2, 3 will be pushed and 2 will be poped

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
        new = Node(data)
        cur = self.head
        if cur is None:
            self.head = new
            return

        while cur.next:
            cur = cur.next

        cur.next = new


    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(nodes) + ']'

    def pop(self):
        cur = self.head
        if cur is None:
            return -1

        temp = cur.data
        self.head = cur.next

        return temp


if __name__ == "__main__":
    t = int(input('no of test cases'))
    for i in range(t):
        n = int(input('no of queries'))
        ar = input('enter query and values')
        ar = [int(e) for e in ar.split()]
        i = 0
        ll = LinkedList()
        while i < (len(ar)):
            if ar[i] == 1:
                ll.append(ar[i+1])
                i += 2
            elif ar[i] == 2:
                print(ll.pop())
                i +=1 
