heap = []

def median(ele):
    #heap.append(ele)
    #heap.sort()
    n = len(heap) 
    if n:
        i = 0
        while i <n:
            if heap[i] > ele:
                break
            i +=1
        heap.insert(i, ele)
                
                
    else:
        heap.append(ele)
        
    mid = len(heap) //2
    if len(heap) %2 == 0:
        
        median_val = (heap[mid-1] + heap[mid])//2

    else:
        median_val = heap[mid]

    return median_val


if __name__ == "__main__":
    a = [5, 15, 1, 3]
    for i in a:
        print('median is {}'.format(median(i)))
