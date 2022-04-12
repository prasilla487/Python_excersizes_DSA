#convert the string to integer, return -1 if string is not numeric
# s = "1234" op: 1234    s ="12ab" op: -1

def atoi(s):
    res = 0
    for i in s:
        if i.isnumeric():
            res = (res * 10) + int(i)
        else:
            res = -1
            break

    return res


s = "123dj4"
print(atoi(s))
