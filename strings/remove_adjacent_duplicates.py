#remove adjacent duplicates from the string
# ex s = "geeksforgeeks" op: gksforgks

def method1(s):
    n = len(s)
    prev = 0
    new = ""
    i = 0
    while i <(n-1):
        print('i is ' + str(i))
        flag = 0
        cur = i + 1
        print('cur is ' + str(cur))
        while s[cur] == s[i] and cur < n-1:
            print('while')
            flag = 1
            cur += 1

        if flag == 0:
            print('if')
            if new != "" and new[-1] != s[i]: 
                print('new' + new[-1])
                new += s[i]
           
            i +=1
        else:
            print('else')
            i = cur

    print(new)

def removeUtil(string, last_removed):
    print('string is  {0} last removed {1}'.format(string, str(last_removed)))
  
    # If length of string is 1 or 0 
    if len(string) == 0 or len(string) == 1: 
        return string 
  
    # Remove leftmost same characters and recur for remaining  
    # string 
    if string[0] == string[1]: 
        last_removed = ord(string[0]) 
        while len(string) > 1 and string[0] == string[1]: 
            string = string[1:] 
        string = string[1:] 
  
        return removeUtil(string, last_removed) 
  
    # At this point, the first character is definiotely different 
    # from its adjacent. Ignore first character and recursively  
    # remove characters from remaining string 
    rem_str = removeUtil(string[1:], last_removed) 
  
    # Check if the first character of the rem_string matches  
    # with the first character of the original string 
    if len(rem_str) != 0 and rem_str[0] == string[0]: 
        last_removed = ord(string[0]) 
        return (rem_str[1:]) 
  
    # If remaining string becomes empty and last removed character 
    # is same as first character of original string. This is needed 
    # for a string like "acbbcddc" 
    if len(rem_str) == 0 and last_removed == ord(string[0]): 
        return rem_str 
  
    # If the two first characters of str and rem_str don't match,  
    # append first character of str before the first character of  
    # rem_str. 
    return ([string[0]] + rem_str) 
  
def remove(string): 
    last_removed = 0
    return toString(removeUtil(toList(string), last_removed)) 
  
# Utility functions 
def toList(string): 
    x = [] 
    for i in string: 
        x.append(i) 
    return x 
  
def toString(x): 
    return ''.join(x) 
  


#s = "acaaabbbacdddd"
s = input('enter string')
print(remove(s))
            
