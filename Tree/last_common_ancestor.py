#last common node of n1 and n2
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.key:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def levelorder(root):
    if root is None:
        return None

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        #print(temp.key,  end=" ")

        if temp.left:
            print('left {}'.format(temp.left.key))
            q.append(temp.left)
        if temp.right:
            print('right {}'.format(temp.right.key))
            q.append(temp.right)

def commonNode(root, n1, n2):
    if root is None:
        return None

    if root.key > n1 and root.key > n2:
        return commonNode(root.left, n1, n2)
    if root.key < n1 and root.key < n2:
        return commonNode(root.right, n1, n2)

    return root
        
#iterative solution
def common(root, n1, n2):
    while root:
        if root.key>n1 and root.key > n2:
            root = root.left
        elif root.key < n1 and root.key < n2:
            root = root.right
        else:
            break
    return root

if __name__ == "__main__":
    root = insert(None, 20)
    insert(root, 8)
    insert(root, 22)
    insert(root, 4)
    insert(root, 12)
    insert(root, 10)
    insert(root, 14)
    levelorder(root)
    common = common(root, 10, 14)
    print('common node is {}'.format(common.key))
        
        
        
