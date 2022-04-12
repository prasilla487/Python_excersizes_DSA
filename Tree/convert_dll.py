#convert binary tree to doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



def convert(root):
    if root is None:
        return root

    if root.left:

        left = convert(root.left)

        while left.right:
            left = left.right

        left.right = root

        root.left = left

    if root.right:

        right= convert(root.right)

        while right.left:
            right = right.left

        right.left = root

        root.right = right


    return root

def btToDll(root):
    if root is None:
        return root

    root = convert(root)

    while root.left:
        root = root.left

    return root
def levelorder(root):
    if root is None:
        return None

    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        print(temp.data, end=" ")

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def print_list(head):
    if head is None:
        return

    while head:
        print(head.data, end=" ")
        head = head.right

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    levelorder(root)
    print('--------------')
    head = btToDll(root)
    print_list(head)
