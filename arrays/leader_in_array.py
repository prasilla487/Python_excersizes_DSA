#leader is if it is greater or equal to the all right elements and the rightmost element

def leader(a):
    for i in range(len(a)):
        greater = 0
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                greater +=1
                break

        if greater == 0:
            print(a[i])

def method(a):
    max_num = 0
    for i in range(len(a)-1, 0, -1):
        if max_num < a[i]:
            max_num = a[i]
            print(max_num)
        

a = [16,17,4,3,5,2]
method(a)
