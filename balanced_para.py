open_list = ['{','[','(']
close_list = ['}',']',')']
string = input("enter string")
stack = []
for i in string:
    if i in open_list:
        stack.append(i)
        print(stack)
    elif i in close_list:
        pos = close_list.index(i)
        print(pos)
        print(open_list[pos]+','+stack[len(stack)-1])
        if len(stack)>0 and open_list[pos] == stack[len(stack)-1]:
            stack.pop()
        else:
            print("unbalanced")
if len(stack) ==0:
    print("balanced")
        
