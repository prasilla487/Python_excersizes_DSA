
mini = -12345
maxi = 12345

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, data):
    data = Node(data)
    if root is None:
        root = data
        return root  

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)

        if temp.left:
            q.append(temp.left)
        else:
            temp.left = data
            return

        if temp.right:
            q.append(temp.right)
        else:
            temp.right = data
            return

def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

def levelorder(root):
    if root is None:
        return None

    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        print(temp.data)

        if temp.left:
            q.append(temp.left)

        if temp.right:
            q.append(temp.right)

def check_util(root, mini, maxi):
    if root is None:
        return True

    if root.data < mini or root.data > maxi:
        return False

    return (check_util(root.left, mini, root.data -1 ) and
           check_util(root.right, root.data + 1, maxi))

def check_bst(root):
    return check_util(root, mini, maxi)

if __name__ == "__main__":
    root = insert(None, 6)
    insert(root, 4)
    insert(root, 9)
    insert(root, 3)
    insert(root, 5)
    insert(root, 7)
    insert(root, 10)
    levelorder(root)
    print(check_bst(root))
    

            
