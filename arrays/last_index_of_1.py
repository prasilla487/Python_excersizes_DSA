#find the last index of 1 ex: a= 00001 op:4

def last_index(s,x):
    flag = False
    index = 0
    i = 0
    for letter in s:
        if letter == x:
            flag = True
            index = i

        i +=1

    if flag:
        print(index)
    else:
        print('-1')

s = '00'
last_index(s, '1')


    
