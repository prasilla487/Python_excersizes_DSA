class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def count_leaves(root, res):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        print(root.data)
        return 1

    ll = count_leaves(root.left, res)
    lr = count_leaves(root.right, res)

    res[0] = max(ll + lr, res[0])

    return res[0]

if __name__=="__main__":
    root = Node(4)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.right=Node(34)
    root.left.left.left = Node(3)
    root.right = Node(10)
    root.right.left = Node(5)
    root.right.right = Node(1)
    print('leaves count is {}'.format(count_leaves(root, [-1234])))
