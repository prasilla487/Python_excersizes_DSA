class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


def addGreaterValue(root, sum_no):
    if root is None:
        return None
    print("sum is {0}".format(sum_no[0]))

    addGreaterValue(root.right, sum_no)

    sum_no[0] = sum_no[0] + root.key

    root.key = sum_no[0]

    addGreaterValue(root.left, sum_no)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(13)

    inorder(root)
    print('------------------')
    sum_num = [0]
    addGreaterValue(root, sum_num)
    inorder(root)
    
