#the tree should mirror image to itself

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def symmetric(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    q = []
    q.append(root)
    q.append(root)

    leftnode = 0
    rightnode = 0

    while ( len(q)):
        print('----------------------')
        leftnode = q.pop(0)
        rightnode = q.pop(0)

        if leftnode.data != rightnode.data:
            return False

        if leftnode.right and rightnode.left:
            q.append(leftnode.right)
            q.append(rightnode.left)

        elif leftnode.right or rightnode.left:
            return False

        if leftnode.left and rightnode.right:
            q.append(leftnode.left)
            q.append(rightnode.right)

        elif leftnode.left or rightnode.right:
            return False


    return True

def recursive(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return recursive(root1.left, root2.right) and recursive(root1.right, root2.left)

    return False

def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight < rheight:
        return lheight + 1
    else:
        return rheight + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left =Node(5)
    root.right.right = Node(3)
    print(height(root))
