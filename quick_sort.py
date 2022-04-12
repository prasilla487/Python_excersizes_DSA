def partition(ar, low, high):
    i = (low-1)
    pivot = ar[high]

    for j in range(low, high):
        if ar[j]<=pivot:
            i +=1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i+1], ar[high] = ar[high], ar[i+1]
    return (i+1)

def quicksort(ar, low, high):
    if low < high:

        pi = partition(ar, low, high)
        quicksort(ar, low, pi-1)
        quicksort(ar, pi+1, high)
        
l = [9,5,1,7,4,2,8,3,6]
print(l)
quicksort(l, 0, len(l)-1)
print(l)
