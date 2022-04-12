#equilibrium is the position where the sum of elements
#before it is equal to the sum of elements after to it
# ex : a = [1,3,5,2,2] op: 5 [1+3] == [2 + 2]

def find_equ(a):
    flag = True
    for i in range(len(a)):
        print('i is {0}, sum1 {1}, sum2 {2}'.format(i, sum(a[:i]), sum(a[i+1:])))
        if sum(a[:i]) == sum(a[i+1:]):
            print(a[i])
            print(i)
            flag = False
            break
            
    if flag:
        print('no equilibrium point')
            

a = [1,2,3]
find_equ(a)
