#connect nodes at same level print if adjacent node exists else -1

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.nextRight = None


def connect(root):
    if root is None:
        return

    q = []
    q.append(root)
    temp = None
    while len(q):
        n = len(q)
        for i in range(n):
            prev = temp
            temp = q.pop(0)

            if i > 0:
                prev.nextRight = temp

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        temp.nextRight= None


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(6)
    connect(root)
    print("nextRight of {0} is {1}".format(root.key, root.nextRight.key if root.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.left.key, root.left.nextRight.key if root.left.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.right.key, root.right.nextRight.key if root.right.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.left.left.key,  root.left.left.nextRight.key if root.left.left.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.left.right.key,  root.left.right.nextRight.key if root.left.right.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.right.left.key,  root.right.left.nextRight.key if root.right.left.nextRight else -1))
    print("nextRight of {0} is {1}".format(root.right.right.key,  root.right.right.nextRight.key if root.right.right.nextRight else -1))
    
