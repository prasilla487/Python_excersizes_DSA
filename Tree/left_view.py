class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(root):
    if root is None:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def levelorder(root, height):
    if root is None:
        return None

    s = []
    s.append(root)
    while len(s) !=0:
        temp = s.pop(0)
        print(temp.data, end=" ")
        if temp.left: 
            s.append(temp.left)
        if temp.right:
            s.append(temp.right)

def height(root):
    if root is None:
        return 0

    left_h = height(root.left)

    right_h = height(root.right)

    if left_h > right_h:
        return left_h + 1
    else:
        return right_h + 1
    
#recursive approach for level order
def printLevelOrder(root):
    ht = height(root)
    for i in range(1, ht+1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return None

    if level == 1:
        print(root.data, end = " ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def insert(root,data):
    data = Node(data)
    if root is None:
        root = data
        return root

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.left is not None:
            q.append(temp.left)
        else:
            temp.left = data
            return

        if temp.right is not None:
            q.append(temp.right)
        else:
            temp.right = data
            return

def leftViewUtil(root, level, max_level):
    if root is None:
        return None

    print('max level is {}'.format(max_level))

    if max_level[0] < level:
        print(root.data)
        max_level[0] = level

    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)


def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)

if __name__ == "__main__":
    t = int(input('no of testcases'))
    for i in range(t):
        s = input('enter the nodes')
        n = [int(e) for e in s.split()]
        root = insert(None, n[0])
        for i in n[1:]:
            insert(root, i)

        #levelorder(root, height(root))
        leftView(root)
        print('/n')
