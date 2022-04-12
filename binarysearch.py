def bs(l,val):
    first=0
    last = len(l)-1
    index = -1
    while (first<=last) and (index ==-1):
        mid = (first+last)//2
        if l[mid] == val:
            index  = mid
            break
        else:
            if val<l[mid]:
                last = mid-1
            else:
                first = mid+1
    return index

def jumpsearch(l, val):
    right, left = 0,0
    import math
    length = len(l)
    jump = int(math.sqrt(length))
    while left<length and l[left]<=val:
        print("left",left)
        print("jump",jump)
        right = min(length-1, left+jump)
        print("right",right)
        if l[left]<=val and l[right]>=val:
            break
        left +=jump
    if left>=length or l[left]>val:
        return None
    right = min(length-1, right)
    i = left
    while i<=right and l[i]<=val:
        if l[i] == val:
            return i
        i +=1

def fibnocisearch(l, val):
    length = len(l)
    fbm2 = 0
    fbm1 = 1
    fbm = fbm1 + fbm2
    while fbm < length:
        fbm2 = fbm1
        fbm1 = fbm
        fbm = fbm1 + fbm2
    index = -1
    while fbm >1:
        i = min(index+fbm2, len(l)-1)
        if l[i] < val:
            fbm = fbm1
            fbm1 = fbm2
            fbm2 = fbm-fbm1
            index = i
        elif l[i] > val:
            fbm = fbm2
            fbm1 = fbm1 - fbm2
            fbm2 = fbm - fbm1
        else:
            return i+1
    if fbm1 and index<(length-1) and l[index+1] == val:
        return index+1
    
print(fibnocisearch([10,20,30,40,50,60,70,80], 10))
