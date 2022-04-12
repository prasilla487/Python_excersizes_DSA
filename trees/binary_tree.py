class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

#iterative method for inorder
def in_order(root):
    s = []
    cur = root
    while True:

        if cur is not None:
            s.append(cur)
            cur = cur.left
        elif(s):
            cur = s.pop()
            print(cur.data)
            cur = cur.right
        else:
            break

def preOrder(root):
    if root is None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def levelOrder(node):
    h = height(node)
    for i in range(1, h+1):
        printLevelOrder(node, i)

def printLevelOrder(node, level):
    if node is None:
        return

    if level ==1:
        print(node.data)
    elif level >1:
        printLevelOrder(node.left, level-1)
        printLevelOrder(node.right, level-1)

def insert(root, key):
    q = []
    q.append(root)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

def delete(root):
    if root is None:
        return

    delete(root.right)
    print(root.key)

def deleteDeepestNode(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
        

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        deleteDeepestNode(root, temp)
        key_node.data = x

    return root

#print line by line using iterative method
def linelevel(root):
    if root is None:
        return None
    #define a list
    q = []

    #append root value to the list
    q.append(root)

    #intialize height
    height = 0

    while(True):
        nodecount = len(q)

        if nodecount == 0:
            return height

        height +=1

        while(nodecount >0):
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            nodecount -=1

        print(' ')
        
        
def printpostorder(inorder, preorder, n): 
    print("called with {0}, {1}, {2}".format(inorder, preorder, n))
    if preorder[0] in inorder: 
        root = inorder.index(preorder[0]) 
          
    if root != 0: # left subtree exists 
        printpostorder(inorder[:root],  
                       preorder[1:root + 1],  
                       len(inorder[:root])) 
      
    if root != n - 1: # right subtree exists 
        printpostorder(inorder[root + 1:],   
                       preorder[root + 1:],  
                       len(inorder[root + 1:])) 
      
    print(preorder[0])
    
if __name__ =="__main__":
        inorder = [4, 2, 5, 1, 3, 6]; 
        preorder = [1, 2, 4, 5, 3, 6]; 
        n = len(inorder) 
        print("Postorder traversal ")
        printpostorder(inorder, preorder, n) 
