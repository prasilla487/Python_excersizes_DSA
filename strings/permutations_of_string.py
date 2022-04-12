def toString(l):
    return ''.join(l)

result = []
e = []

def permutation(s, l, r):
    if l == r:
        print(toString(s))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permutation(a, l+1, r)
            a[l], a[i] = a[i], a[l]

s = 'ABCDEFA'
a = list(s)
permutation(a, 0, len(s)-1)
