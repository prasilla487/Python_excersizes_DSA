#max of all subarrays of size k
#inp :1 2 3 2 1 4 5 6 k = 3 op: 3 3 3 4 5 6

def maxOfSubarray(ar, k):
    n = len(ar)
    for i in range(n):
        if len(a[i:(k+i)]) == k:
            #print(a[i:(k+i)])
            print(max(a[i:(k+i)]) , end = " ")


#a = [1,2,3,1,4,5,2,3,6]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
maxOfSubarray(a, 3)
