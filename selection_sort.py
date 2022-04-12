def selectionsort(l):
    for i in range(len(l)):
        min = 2030
        for j in range(i, len(l)):
            if l[j] < min:
                min = l[j]
        l[l.index(min)], l[i]= l[i],min
        
        print(l)

l=[14,33,27,10,35,19,42,44]
print(l)
selectionsort(l)
print(l)
