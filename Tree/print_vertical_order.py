class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, data):
    key = Node(data)

    if root is None:
        root = key
        return root

    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)

        if temp.left is None:
            temp.left = key
            return
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right =  key
            return
        else:
            q.append(temp.right)

def findMinMax(root, minimum, maximum, hd):

    if root is None:
        return

    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    findMinMax(root.left, minimum, maximum, hd-1)
    findMinMax(root.right, minimum, maximum, hd + 1)
    
def printVerticalLine(root, line_no, hd):
    if root is None:
        return
    print('data is {}'.format(root.key))

    if hd == line_no:
        print(root.key, end = " ")

    printVerticalLine(root.left, line_no, hd-1)
    printVerticalLine(root.right, line_no, hd +1)


def verticalOrder(root):

    minimum = [0]
    maximum = [0]

    findMinMax(root, minimum, maximum, 0)

    for line_no in range(minimum[0] , maximum[0] + 1):
        printVerticalLine(root, line_no, 0)
        print('\n')

def filldict(node, hd, dic):

    if node is None:
        return

    if hd in dic.keys():
        dic[hd].append(node.key)
    else:
        dic[hd] = [node.key]

    filldict(node.left, hd-1, dic)
    filldict(node.right, hd+1, dic)

#using dictionary
def method2(root):

    dic = {}

    filldict(root, 0, dic)

    for i in dic.keys():
        print(dic[i])
        print('\n')
    
        


if __name__ == "__main__":
    root = insert(None, 1)
    insert(root, 2)
    insert(root, 3)
    root.left.left = Node(4)
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.right.left.right = Node(8) 
    root.right.right.right = Node(9)
    method2(root)
        
