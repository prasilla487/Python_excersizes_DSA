#find the lognest substring with distinct letters
#geeksforgeeks op: length is 7, eksforg

def findLongest(s):
    res = 0
    n = len(s)

    l = []

    for i in range(n):
        print("list is {0}".format(l))
        for j in range(i, n):

            if s[j] in l:
                print('in')
                break

            else:
                print('else')
                res = max(res, j-i+1)
                print('res is {0}'.format(res))
                l.append(s[j])
        print('-----')

        l.remove(s[i])


    return res

#linear time o(n)
def method2(s):
    lastIndex = [-1] * 256

    res = 0
    start = 0
    n = len(s)

    for i in range(n):
        print(lastIndex)

        start = max(start, lastIndex[ord(s[i])] + 1)
        print("start is {0}".format(start))

        res = max(res, i - start +1)
        print("res is {0}".format(res))

        lastIndex[ord(s[i])] = i

    return res

s = "geeksforgeeks"
res = method2(s)
print(res)
