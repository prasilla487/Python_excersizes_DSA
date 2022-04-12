#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# a= [2,0,2]
# output: 2 we can store two blocks of water in between 2, 2

def compute_water(a):
    n = len(a)
    count = 0
    for i in range(1,n-1):
        
        left = a[i]
        #find the maximum left
        for j in range(i):
            left = max(left, a[j])

        right = a[j]
        #find the maximum right
        for j in range(i+1, n):
            right = max(right, a[j])


        count = count + (min(left, right) - a[i])

    print(count)

def method2(a):
    n = len(a)
    count = 0
    #intailize two arrays as left and right to store max values

    left =[0] * n

    right = [0] * n

    left[0] = a[0]
    for i in range(1, n):
        left[i] = max(left[i-1], a[i])

    right[n-1] = a[n-1]
    for j in range(n-2, -1, -1):
        right[j] = max(right[j+1], a[j])

    for i in range(n):
        count += min(left[i], right[i]) - a[i]

    print(count)


    


if __name__ == "__main__":
    a = [3,0,2,0,4]
    method2(a)
