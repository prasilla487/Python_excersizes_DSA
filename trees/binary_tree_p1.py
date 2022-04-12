class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

#iterative method
def levelorder(root):
    if root is None:
        return

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        print(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def delete_deepest(root,d_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
            


def delete(root, key):
    if root is None:
        return None
    if root.left == None and roor.right == None:
        return None

    q = []
    key_node = None
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)

        if temp.right:
            q.append(temp.right)

    
    if key_node:
        x = temp.data
        delete_deepest(root,temp)
        key_node.data = x
    
        
def iterative_inorder(root):
    cur = root

    while cur is not None:
        if cur.left is None:
            print(cur.data)
            cur = cur.right
        else:
            pre = cur.left
            while(pre.right is not None and pre.right !=cur):
                pre = pre.right

            if pre.right is None:
                pre.right = cur
                cur = cur.left

            else:
                pre.right = None
                print(cur.data)
                cur = cur.right

def insert(root, key):
    data = Node(key)
    if root is None:
        root = data
        return 
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.left is None:
            temp.left = data
            return 
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = data
            return 
        else:
            q.append(temp.right)
        

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    insert(root, 6)
    insert(root, 7)
    insert(root, 8)
    iterative_inorder(root)
