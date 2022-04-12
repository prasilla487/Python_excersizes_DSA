class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def list_to_bst(arr):
    if not arr:
        return None

    mid = len(arr)//2
    root = Node(arr[mid])

    root.left = list_to_bst(arr[:mid])
    root.right = list_to_bst(arr[mid+1:])
    return root


def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def  preorder(root):
    if root is None:
        return None

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

if __name__== "__main__":
    l = [1,2,3,4,5]
    root = list_to_bst(l)
    preorder(root)
