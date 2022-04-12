class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    
    else:
        root.right = insert(root.right, key)
    
    return root

def preorder(root):
    if root is None:
        return None
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return None
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

if __name__ == "__main__":
    pre = [10, 5, 1, 7, 40, 50]
    root = Node(pre[0])
    for i in pre[1:]:
        root = insert(root, i)
    
    inorder(root)