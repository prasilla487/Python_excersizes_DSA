def insertion(l):
    for i in range(len(l)):
        for j in range(0, i):
            if l[j]>l[i]:
                l[j], l[i] = l[i], l[j]
#l = [9,5,1,7,4,2,8,3,6]
l=[14,33,27,10,35,19,42,44]
print(l)
insertion(l)
print(l)




