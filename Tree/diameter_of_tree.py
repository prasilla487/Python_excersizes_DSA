#longest path from one leave to other leave
class Node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    print(diameter(root))
    
