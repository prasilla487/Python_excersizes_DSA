import sys
class Node:
    def __init__(self, key):
        self.key = key
        self.hd = sys.maxsize
        self.left = self.right = None


def insert(root, data):
    key = Node(data)
    if root is None:
        root = key
        return root

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)

        if temp.left:
            q.append(temp.left)
        else:
            temp.left = key
            return

        if temp.right:
            q.append(temp.right)
        else:
            temp.right = key
            return

def levelorder(root):
    if root is None:
        return None

    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        print(temp.key)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def viewBottom(root):
    if root is None:
        return None

    q = []
    q.append(root)

    dic = {}

    while len(q):

        temp = q.pop(0)

        hd = temp.hd

        dic[hd] = temp.key

        if temp.left:
            q.append(temp.left)
            temp.left.hd = hd - 1

        if temp.right:
            q.append(temp.right)
            temp.right.hd = hd + 1

    for i in dic.keys():
        print(dic[i], end = " ")
    


if __name__ == "__main__":
    root = insert(None, 20)
    insert(root, 8)
    insert(root, 22)
    insert(root, 5)
    insert(root, 3)
    insert(root, 4)
    insert(root, 25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    levelorder(root)
    viewBottom(root)
