def shellSort(nlist):
    gap = len(nlist)//2

    while gap>0:
        for start in range(gap):
            gap_insertsort(nlist, start, gap)
        
        gap = gap //2


def gap_insertsort(ar, start, gap):
    for i in range(start+gap, len(ar), gap):
        cur_value = ar[i]
        pos = i

        while pos>=gap and ar[pos-gap] >= ar[pos]:
            ar[pos] = ar[pos-gap]
            pos = pos-gap

        ar[pos]=cur_value

nlist = [5,8,1,3,4,2,7,9]
#nlist = [5,3,1,2]  
shellSort(nlist)
print(nlist)
