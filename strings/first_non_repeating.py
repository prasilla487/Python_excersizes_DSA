def first_non(s):
    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] +=1

    for key, val in zip(d.keys(), d.values()):
        if val == 1:
            return print(key)


    return print(-1)


s = "xyz"
first_non(s)
