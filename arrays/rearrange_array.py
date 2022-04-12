#rearrange array in the order of first element should be max value, second should be min value, third should be second max, fourth should be second min and so on
#using a auxilary array
def rearrange_method1(a):
    temp = [0]*(len(a))
    small = 0
    large = len(a)-1
    for i in range(len(a)):
        if i%2 == 0:
            temp[i] = a[large]
            large -=1
        else:
            temp[i] = a[small]
            small +=1
    a = temp
    print(a)

#using only O(1) extra space
def rearrange(arr, n): 
  
    max_index = n-1
    min_index = 0
    max_element = arr[max_index] + 1
    for i in range(0,n):
        if i%2 == 0:
            arr[i] += (arr[max_index] % max_element) * max_element
            max_index -=1

        else:
            arr[i] += (arr[min_index] % max_element ) * max_element
            min_index +=1

    for i in range(0,n):
        arr[i] = arr[i]//max_element

    print(arr)

a = [1,2,3,4,5,6,7,8,9]
rearrange(a, len(a))
