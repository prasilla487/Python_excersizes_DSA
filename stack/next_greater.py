#print next greater element of every element, if no greater element -1
# 1 3 2 4 op: 2 4 4 -1
def nextGreater(a):
    for i in range(len(a)):
        flag = 0
        for j in range(i, len(a)):

            if a[j] > a[i]:
                flag = 1
                print(a[j])
                break

        if not flag:
            print(-1) 

a = [13,7,6,12]
nextGreater(a)
            
            
        
