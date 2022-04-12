def bubblesort(ar):
    for j in range(len(ar)-1):
        for i in range(len(ar)-1):
            if ar[i]>ar[i+1]:
                ar[i], ar[i+1] = ar[i+1], ar[i]

ar = [7,4,8,1,9,3,5,2,6]
print(ar)
bubblesort(ar)
print(ar)
