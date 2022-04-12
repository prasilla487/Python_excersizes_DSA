#remove common characters of s1 and s2 from s1 and concatenate both strings

def remove(s1, s2):
    seen = []
    new = ""
    for char in s1:
        if char in s2:
            seen.append(char)
        else:
            new +=char
    for char in s2:
        if char in seen:
            continue
        else:
            new +=char

    return print(new)

s1 = 'common'
s2 = 'concatenate'
remove(s1, s2)
            
