#there are two strings, check whether string a can be obtained by rotating
#string b two places

def check(str1, str2):
    if len(str1) != len(str2):
        return False

    clock_root =""
    anticlock_root = ""

    clock_root += str2[-2:] + str2[0:-2]
    anticlock_root += str2[2:] + str2[0:2]

    return (str1 == clock_root or str2 == anticlock_root)


str1 = "geeks"
str2 = "egeks"
if check(str1, str2):
    print('yes')
else:
    print('no')
