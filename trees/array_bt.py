tree = [0 for x in range(10)]

def root(root):
    if tree[0] == 0:
        tree[0] = root
    else:
        print("Tree already had root")

    return 0

def set_right(child, parent):
    if tree[parent]:
        tree[(2*parent)+2] = child
        return
    else:
        print("can't insert child {0} parent is not found".format(parent))

def set_left(child, parent):
    if tree[parent]:
        tree[(2*parent)+1] = child
        return
    else:
        print("can't insert child {0} parent is not found".format(parent))


def print_tree():
    for i in tree:
        print(i)

if __name__=="__main__":
    root('A')
    set_left('B',0)
    set_right('C',0)
    set_right('E', 1)
    set_left('D', 1)
    set_right('F', 2)
    print_tree()
