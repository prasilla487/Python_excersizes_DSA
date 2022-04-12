def repeated_char(s):
    d = {}

    for char in s:
        if char not in d.keys():
            d[char] = 1
        else:
            d[char] +=1

    for key, val in zip(d.keys(), d.values()):
        if val > 1:
            return print(key)

    return print(-1)

s = "geeksforgeeks"
repeated_char(s)
