class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    node = Node(key)
    if root is None:
        root = node
    else:
        if root.data < key:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, key)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    cur = root
    s = []
    while True:
        if cur is not None:
            s.append(cur)
            cur = cur.left
        
        elif (s):
            cur = s.pop()
            print(cur.data)
            cur = cur.right
        else:
            break


#second method to insert
def insert_node(node, key):
    if node is None:
        return Node(key)
    
    if key < node.data:
        node.left = insert_node(node.left, key)
    else:
        node.right = insert_node(node.right, key)
    
    return node

def get_minimum(root):
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur


def delete(root,  key):
    if root is None:
        return root
    
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        min_node = get_minimum(root.right)

        root.data = min_node.data

        root.right = delete(root.right, min_node.data)

    return root

if __name__=="__main__":
    root = None
    root = insert_node(root, 50)
    root = insert_node(root, 30)
    root = insert_node(root, 20)
    root = insert_node(root, 40)
    root = insert_node(root, 60)
    root = insert_node(root, 80)
    root = insert_node(root, 70)
    delete(root, 30)
    inorder(root)