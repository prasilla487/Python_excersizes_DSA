s = ["1,3,9,7,13","1,2,4,-13,15"]
news = ""
def letterChange():
    for l in range(len(s)):
        st = s[l]
        if st.isalnum() and st.isdigit() != True :
            st =  chr(ord(s[l].upper())+32+1)
        if st in ['a','e','i','o','u']:
            st = st.upper()
        news +=st

def findinter(s):
    list1 = [abs(int(x)) for x in s[0].split(',')]
    list2 = [abs(int(y)) for y in s[1].split(',')]
    set1 = set(list1)
    print(set1)
    set2 = set(list2)
    print(set2)
    inter = sorted(set1 &set2)
    i = [str(x) for x in inter]
    if len(inter):
        print(','.join(i))
    else:
        return False

def questionmark():
    s ="9???1???9??1???9"
    qs = "???"
    print(len(s))
    if qs in s:
        bn = (s.rindex(qs))
        for i in range(bn, 0, -1):
            if s[i].isdigit():
                bn = s[i]
                break

        af = (s.rindex(qs))
        for j in range(af,len(s)):
            if s[j].isdigit():
                print(s[j])
                af = s[j]
                break
        if int(bn)+int(af)<=10:
            return True
        else:
            return False

def alphabetsoup():
    s = "hello"
    st = list(s)
    st.sort()
    print(st)
    
def longestword():
    sen = "fun&!! hello"
    sen1 = sen.split(' ')
    t = [len(x) if x.isalpha() else 0 for x in sen1]
    print(t)
    print(sen1[t.index(max(t))])

def reverse():
    s = "Hello World and Coders"
    print(s[::-1])

def substring():
    s = "ABCDCDC"
    a = "CDC"
    count = 0
    if a in s:
        ind = s.index(a)
        for i in range(ind, len(s)):
            if a == s[i:(i+len(a))]:
                count +=1
    print(count)

def strfunc():
    s ="abc12#"
    l = [s.isalnum(), s.isalpha(), s.isdigit(), s.islower(), s.isupper()]
    for i in l:
        print(i)

strfunc()
