#return tree is balanced if the difference between height of left subtree is right
#subtree is not more than 1

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left) , height(root.right))

def check_balanced(root):
    if root is None:
        return True


    lh = height(root.left)
    rh = height(root.right)

    diff = lh - rh
    if diff > 1:
        return False

    return check_balanced(root.left) and check_balanced(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.left.left = Node(40)
    root.right = Node(30)
    root.right.left = Node(80)
    print(check_balanced(root))

    
