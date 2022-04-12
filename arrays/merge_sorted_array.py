def merge(ar, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(n1):
        l1[i] = ar[start+i]

    for j in range(n2):
        l2[j] = ar[mid+j+1]

    i = 0
    j =0
    k = start

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            ar[k] = l1[i]
            i +=1
            k +=1
        else:
            ar[k] = l2[j]
            j +=1
            k +=1

    while i < n1:
        ar[k] = l1[i]
        i +=1
        k +=1

    while j < n2:
        ar[k] = l2[j]
        j +=1
        k +=1
        


def mergeSort(ar, start, end):
    if start < end:
        mid = (start + (end-1))//2
        mergeSort(ar, start, mid)
        mergeSort(ar, mid+1, end)
        merge(ar, start, mid, end)
    
a = [5,3,4,1,6,2]
mergeSort(a, 0, len(a)-1)
print(a)
