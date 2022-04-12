class Lnode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Tnode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def push(head, new_node):

    #allocate node
    node = Lnode(new_node)

    #link the old list to new node
    node.next = head

    #make new_node as head
    head = node

    return head

def print_list(head):
    cur = head
    while cur !=None:
        print(cur.data)
        cur = cur.next

def convertToBst():
    global head
    temp = head
    count = 0
    while temp != None:
        temp = temp.next
        count +=1

    return convertToBstRecur(count)

def convertToBstRecur(n):
    global head
    if n<=0:
        return None

    #construct the left tree first
    left = convertToBstRecur(int(n/2))

    #make head as new root
    root = Tnode(head.data)

    #append the left sub tree to the root.left
    root.left = left

    head = head.next

    root.right = convertToBstRecur(n-int(n/2)-1)

    return root

def preorder(root):
    if root is None:
        return None

    print(root.key, end=" ")
    preorder(root.left)
    preorder(root.right)

   

if __name__=="__main__":
    head = None
    head = push(head,7)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    print_list(head)
    root = convertToBst()
    preorder(root)
    
