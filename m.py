def sum():
    m=7
    t=4
    mg = "two times three is not four two"
    mg = mg.split(' ')
    tr = "two times Two is four"
    tr = tr.split(' ')
    tr_set = list(set(tr))
    c = 0
    for word in (tr_set):
        if tr.count(word) == mg.count(word):
            if tr[tr.index(word)] == mg[mg.index(word)]:
                c +=1
    if c == len(tr_set):
        print("Yes")
    else:
        print("No")

def ejj():
    n, m = 5,3
    l = [0]*(n+1)
    q = [[1,2,100],[2,5,100],[3,4,100]]
    for i in range(len(q)):
        l[q[i][0]-1] +=q[i][2]
        l[q[i][1]] -=q[i][2]
        print(l)
    max = a = 0
    for i in l:
        a +=i
        print(a)
        print(max)
        if max<a:
            max=a
    print(max)

def counter_string():
    m=7
    t=4
    mg = "two times three is not four two"
    mg = mg.split(' ')
    tr = "two times two is four"
    tr = tr.split(' ')
    from collections import Counter
    c =((Counter(tr)-Counter(mg)))
    if c == {}:
        print("yes")
    else:
        print("no")

counter_string()
