#form large number from an array
#ex : a = [3 30 34 5 9] op: 9534330
result = [0]

def toString(a):
    a = [str(e) for e in a]
    return ''.join(a)

def permutation(a,l,r):
    if l==r:
        value = toString(a)
        if int(value) > result[0]:
            result[0] = int(value)
        
    else:
        for i in range(l, r+1):
            a[i], a[l] = a[l], a[i]
            permutation(a, l+1, r)
            a[i], a[l] = a[l], a[i]


s = input('enter')
a = [int(e) for e in s.split( )]
permutation(a, 0, len(a)-1)
print(result)
