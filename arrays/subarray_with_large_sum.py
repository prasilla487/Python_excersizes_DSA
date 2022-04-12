from sys import maxsize

def max_sum(a):
    global_sum = -maxsize - 1
    cur_sum = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, len(a)):
        cur_sum +=a[i]

        if cur_sum <0:
            cur_sum = 0
            s = i + 1
        elif global_sum < cur_sum:
            global_sum = cur_sum
            start = s
            end = i

    print(global_sum)
    print(a[start:end])
    
a = [-2,-3,4,-1,-2,1,5,-3]
max_sum(a)


    
