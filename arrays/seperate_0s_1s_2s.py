def seperate(a):
    low = 0
    mid = 0
    high = len(a)-1

    while mid<= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid] , a[low]
            low +=1
            mid +=1
        elif a[mid] ==1:
            mid +=1
        else:
            a[high], a[mid] = a[mid], a[high]
            high -=1
    print(a)



a = [0,2,1,2,1,2,0,1]
seperate(a)
