#remove duplicates from string without changing the order

def removeDuplicate(s):
    n = len(s)
    i = 0
    new = ""
    while i < n:
        if s[i] not in s[:i]:
            new += s[i]
        i +=1


    print(new)


s = "geeksforgeeks"
removeDuplicate(s)
            
            
            
