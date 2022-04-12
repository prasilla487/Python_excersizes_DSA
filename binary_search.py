a = [44, 35,42,27,10,14,19,26,31,33]
value = 100
a.sort()
low = 0
high = len(a)-1
c=0
mid = (low + high)//2
while low<len(a):
    mid = (low + high)//2
    if a[mid] == value:
        print("found")
        c +=1
        break
    elif a[mid]<value:
        low = mid+1
    elif a[mid]>value:
        high = mid-1

if c == 0:
    print("notfound")
