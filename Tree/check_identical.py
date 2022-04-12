class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

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

def compare(root, second):
    if root is None or second is None:
        return

    q = []
    s = []
    s.append(second)
    q.append(root)

    Flag = 0

    while len(q):
        temp = q.pop(0)
        second = s.pop(0)
        if temp.data != second.data:
            return False

        if temp.left and second.left:
            Flag = 1
            q.append(temp.left)
            s.append(second.left)

        if temp.right and second.right:
            Flag = 1
            q.append(temp.right)
            s.append(second.right)
    
    if Flag:
        return True
    else:
        return False

        

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(3)
    root.right.right = Node(10)
    #levelorder(root)

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.right = Node(3)
    root1.right.right = Node(10)
    a = compare(root,root1)
    if a:
        print('Identical')
    else:
        print('Not Identical')
