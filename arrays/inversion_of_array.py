#count the required no of inversions required to sort an array
# example : a = [3,2,1] to sort 2 inversions required (3,2) (3,1)

def count_inversions(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                count +=1
                print("the pair is {0}, {1}".format(a[i], a[j]))

    print(count)


def inversions(a, n):
    temp = [0] * n

    return merge_inversions(a, temp, 0, n-1)

def merge(arr, temp_arr, low, mid, high):
    print("merge --- {0}, {1}, {2}, {3},{4}".format(arr,temp_arr, low, mid, high))
    i = low
    j = mid +1
    k = low
    count = 0

    while i<= mid and j<=high:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i +=1
            k +=1
        else:
            temp_arr[k] = arr[j]
            count += (mid-i+1)
            j +=1
            k +=1

    while i <= mid:
        temp_arr[k] = arr[i]
        i +=1
        k +=1

    while j <= high:
        temp_arr[k] = arr[j]
        k +=1
        j +=1

    for loop_var in range(low, high+1):
        arr[loop_var] = temp_arr[loop_var]

    return count

def merge_inversions(arr, temp_arr, low, high):
    print("call --------------- {0}, {1}, {2}, {3}".format(arr, temp_arr, low, high))

    count = 0
    if low < high:

        mid = (low + high -1)//2
        count += merge_inversions(arr,  temp_arr, low, mid)

        count += merge_inversions(arr, temp_arr, mid+1, high)

        count += merge(arr, temp_arr, low, mid , high)

    return count

a = [1,20,6,4,5]
count_inversions(a)
c = inversions(a, len(a))
print(a)

                
