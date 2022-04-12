#reverse string without reversing words in it

def reverse_string(string):
    string_arr = string.split('.')
    n = len(string_arr)
    new = ""
    for i in range(n-1, -1, -1):
        if i != 0:
            new += string_arr[i]+'.'
        else:
            new += string_arr[i]

    print(new)

def method2(s):
    new_s = ""
    for i in s.split(' '):
        new_s += i[::-1] + ' '
        print(i[::-1])
    
    s = new_s[::-1]
    print(s)

s = "geeks quiz practice code"
#reverse_string(s)
method2(s)
