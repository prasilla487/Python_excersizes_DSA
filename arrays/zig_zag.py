#array should be arranged in zig zag fashion means in fashion of a<b>c<d>e<f..
# a = [1,4,3,2] op: [1,4,2,3]

def zig_zag(a):
    n = len(a)
    s = '<'
    for i in range(n-1):
        if s == '<':
            s = '>'
            if a[i] > a[i+1]:

                a[i], a[i+1] = a[i+1], a[i]
                
        elif s == '>':
            s = '<'
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        
                

    print(a)

def merge(a, low, mid, high):
    n1 = mid - low +1
    n2 = high -mid

    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(n1):
        l1[i] = a[i+low]

    for j in range(n2):
        l2[j] = a[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i<n1 and j<n2:
        if l1[i] < l2[j]:
            a[k] = l1[i]
            i +=1
            k +=1
        else:
            a[k] = l2[j]
            j +=1
            k +=1

    while i <n1:
        a[k] = l1[i]
        k +=1
        i +=1

    while j<n2:
        a[k] = l2[j]
        j +=1
        k +=1
    


def mergesort(a, low, high):
    if low < high:
        mid = (low + (high-1))//2
        mergesort(a, low, mid)
        mergesort(a, mid+1, high)
        merge(a, low, mid, high)

def method2(a):
    n = len(a)
    #a.sort()
    mergesort(a, 0, n-1)
    for i in range(1,n,2):
        a[i], a[i+1] = a[i+1], a[i]

    print(a)
        
    
a = [4,3,7,8,6,2,1,10,5]
method2(a)
        
