class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_inorder(root, arr):
    if root is None:
        return None

    insert_inorder(root.left, arr)
    arr.append(root.data)
    insert_inorder(root.right, arr)

def arr_to_bst(root, arr):
    if root is None:
        return None

    arr_to_bst(root.left, arr)
    root.data = arr.pop(0)
    arr_to_bst(root.right, arr)

def bt_to_bst(root):

    if root is None:
        return None

    arr = []
    insert_inorder(root, arr)
    arr.sort()

    arr_to_bst(root, arr)


def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.data)
    inorder(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)
    inorder(root)
    print("------------------")
    bt_to_bst(root)
    inorder(root)
