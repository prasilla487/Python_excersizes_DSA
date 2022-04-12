#implement two methods set and get

class Dictionary:
    def __init__(self, size):
        self.dict = {}
        self.size = size

    #key, value
    def set(self, x,y):
        if len(self.dict) != self.size:
            self.dict[x] = y
            print('inserted {0},{1}'.format(x,y))

        else:
            for i in self.dict.keys():
                key = i
                break

            val = self.dict.pop(key)
            print('removed {0},{1}'.format(key,val))
            self.dict[x] = y
            print('inserted {0},{1}'.format(x,y))


    def get(self, key):
        res = -1
        if key in self.dict.keys():
            res = self.dict[key]

        return res


if __name__ == "__main__":
    t = int(input('enter testcases'))
    for i in range(t):
        n = int(input('enter cache size'))
        q = int(input('enter queries'))

        s = input('enter queries')
        inp = []
        for i in s.split():
            if i.isnumeric():
                inp.append(int(i))
            else:
                inp.append(i)

        dic = Dictionary(n)
        j = 0
        while j < len(inp):
            if inp[j] == "SET":
                dic.set(inp[j+1], inp[j+2])
                j +=3
            elif inp[j] == 'GET':
                res = dic.get(inp[j+1])
                print('the value of key {0} is {1}'.format(inp[j+1], res))
                j +=2
            
            
    
            
        
