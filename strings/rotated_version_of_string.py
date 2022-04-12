#print 1 if s2 is rotated version of string s1 else print 0

def rotate(s1, s2):
    new = ""
    if len(s1) != len(s2):
        return print(0)
    
    for i in range(len(s2)):
        new += s2[i+1:] + s2[:i+1]
        #print('new is {}'.format(new))
        if new == s1:
            return print(1)
        new = ""

    return print(0)


#s1 = "geeksforgeeks"
#s2 = "forgeeksgeeks"
s1 = "geekofgeeks"
s2 = "geeksgeekof"
rotate(s1,s2)
    
