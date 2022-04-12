#n = int(input("Enter length"))
#s = int(input("Enter sum"))
def subarray_with_given_sum(n, s, a):  
    first = 1
    last = 1
    equal = False
    for j in a:
        temp_sum = 0
        first = a.index(j)+1
        for i in range(a.index(j),n):
            temp_sum += a[i]
            if temp_sum == s:
                last = i+1
                equal = True
                break
            if temp_sum >s:
                break
        if equal:
            break
    if equal:
        print("first {0}, last {1}".format(first, last))
    else:
        print("-1")

def method(n,s,a):
    start = 0
    end = 0
    s_sum = 0
    while start<n and end <=n:
        print("start {0}, end {1}, sum {2}".format(start, end, s_sum))
        if (s_sum == s):
            print(start+1, end)
            return
        elif s_sum > s:
            s_sum = s_sum - a[start]
            start +=1
        else:
            s_sum += a[end]
            end +=1
    print("-1")

def method2(n, s, a):
    end = 0  
    start = 1
    csum = 0
    flag = 0
    for i in range(n):
        csum += a[i]
        while csum > s:
            csum -=a[end]
            end +=1
        if csum == s:
            print(end+1, i+1)
            flag =1
            break 
        
    if flag == 0:
        print("-1")
        

if __name__ == "__main__":
    t = int(input())
    for i in range(0,t):
        n = int(input("size"))
        s = int(input("sum"))

        inp = input()
        a = [int(element) for element in inp.split()]
        print(a)

        #subarray_with_given_sum(n,s,a)
    n = 57
    s = 1562
    inp = "28 68 142 130 41 14 175 2 78 16 84 14 193 25 2 193 160 71 29 28 85 76 187 99 171 88 48 5 104 22 64 107 164 11 172 90 41 165 143 20 114 192 105 19 33 151 6 176 140 104 23 99 48 185 49 172 65"
    a = [int(element) for element in inp.split()]
    method2(n, s, a)
