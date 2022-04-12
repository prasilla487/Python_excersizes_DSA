def frequent(ar):
    ar = ar.split(' ')
    d = {}
    for word in ar:
        if word in d.keys():
            d[word] +=1
        else:
            d[word] = 1

    max_val = max(d.values())
    word = ""
   
    for key, val in zip(d.keys(), d.values()):
        if val == max_val:
            word += ' '
            word +=key
       
    return word.split(' ')[-1]

#s = "fund for geeks"
s = "geeks for geeks"
print(frequent(s))
