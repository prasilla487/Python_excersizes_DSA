def merge(ar, l, m, h):
    print("mergesort {0} {1} {2}".format(l,m,h))
    n1 = m-l++1
    n2 = h-m

    l1 =  [0] * n1
    l2 = [0] * n2

    for i in range(n1):
        l1[i] = ar[l+i]

    print("---------------")
    for j in range(n2):
        l2[j] = ar[m+j+1]

    i = 0
    j = 0
    k = l
    
    while i <n1 and j <n2:
        if l1[i]<=l2[j]:
            ar[k] = l1[i]
            i +=1
        else:
            ar[k] = l2[j]
            j +=1
        k +=1

    while i<n1:
        ar[k] = l1[i]
        i +=1
        k +=1

    while j<n1:
        ar[k] = l2[j]
        j +=1
        k +=1
    
        


def mergesort(ar, l, h):
    if l<h:
        m = (l+(h-1))//2

        mergesort(ar, l, m)
        mergesort(ar, m+1, h)
        merge(ar, l, m, h)
        
l = [5,2,4,6,1,3]
print(l)
mergesort(l, 0, len(l)-1)
print(l)
