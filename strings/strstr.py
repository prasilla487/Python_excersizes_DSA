#given two strings (s,x) check if x is a substring of s and give the index of first occurence
#s = "manchemprasila" x="prasila" op: 7

def check_substring(s,x):
    i = 0
    n = len(s)
    flag = 0
    while(i < n):
        if s[i] == x[0]:
            m = len(x)
            j = 0
            count = 0
            while j <m:
                if s[i] != x[j]:
                    #count -=1
                    flag = 1
                    break
                count +=1
                i +=1
                j +=1

            if count == m:
                index = i - m
                return index

        i +=1

    if flag:
        return -1

   
        
    

s = "something"
x = "th"
print(check_substring(s,x))
