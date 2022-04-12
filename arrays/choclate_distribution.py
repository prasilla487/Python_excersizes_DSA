import sys

def choclate_distribution(arr, n, m):
    if m ==0 or n== 0:
        return -1

    if n<m:
        return -1

    i = 0

    arr.sort()
        
    min_diff = sys.maxsize
    while(i+m-1 < n):
        diff = arr[i+m-1] - arr[i]
        if diff < min_diff:
            min_diff = diff


        i +=1


    return min_diff


if __name__ == "__main__":
    a = input('enter arry')
    arr = [int(element) for element in a.split()]
    m = int(input("enter students no"))
    d = choclate_distribution(arr, len(arr), m)
    print(d)
