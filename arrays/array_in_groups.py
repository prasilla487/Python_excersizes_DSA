#reverse every sub-array of k group elements

def reverseSubarray(a, k):
    count = 1
    full = []
    temp = []
    n = len(a)
    for i in range(n):
        temp.insert(0, a[i])
        if count == k:
            count = 0
            full.extend(temp)
            temp = []
        count +=1

    if temp != []:
        full.extend(temp)
        
    print(full)

def method2(a, k):
    i = 0
    n = len(a)

    while i<n:
        left = i

        right = min(i+k-1, n-1)

        while left < right:
            a[left], a[right] = a[right], a[left]
            left +=1
            right -=1

        i +=k


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    #reverseSubarray(a, 5)
    method2(a, 5)
    print(a)
        
