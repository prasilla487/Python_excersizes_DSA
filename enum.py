import enum

class Objenum(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


def order():
    li = []
    for value in Objenum:
        li.append(value.value)
    li.sort()
    i = 0
    while i <(len(li)):
        for value in Objenum:
            if value.value == li[i]:
                print(value.name)
        i +=1

if __name__=="__main__":
    words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
    ]
    dic = {}
    for word in words:
        dic[word] = words.count(word)
    li = [y for y in dic.values()]
    li.sort()
    li = li[-4:]
    print(li)
    for name, val in dic.items():
        if val in li:
            li[li.index(val)]= ""
            print('( {}, {})'.format(name, val))
        
