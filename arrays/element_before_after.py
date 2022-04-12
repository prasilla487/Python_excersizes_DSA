#find element before which all elements are smaller and element after which all
#elements are greater than
# a = [5, 1,4,3,6,8,10,7,9] o/p : 6

def find(a):
    n = len(a)
    flag = 0
    for i in range(1,n):
        j = 0
        k = n-1
        flag = 1
        while(j<i or k > i):
            if a[j] > a[i]:
                flag = 0
                break
            elif a[k] < a[i]:
                flag = 0
                break
            else:
                j +=1
                k -=1

        if flag:
            print(a[i])
            return

    if not flag:
        print('-1')

#optimized solution
def findElement(arr, n):  
   
    # leftMax[i] stores maximum of arr[0..i-1]  
    leftMax = [None] * n  
    leftMax[0] = float('-inf')
  
    # Fill leftMax[]1..n-1]  
    for i in range(1, n):  
        leftMax[i] = max(leftMax[i-1], arr[i-1])

    rightMin = float('inf')


#a = input('enter arry')
#ar = [int(e) for e in a.split()]
ar = [5, 1, 4, 3, 6, 8, 10, 7, 9]
findElement(ar, len(ar))
            
