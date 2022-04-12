class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr___(self):
        return repr(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.min = None
        self.count = 0

    def push(self, value):
        
        if self.top is None:
            self.top = Node(value)
            self.min = value

        elif value < self.min:
            temp =  (2*value) - self.min
            new = Node(temp)
            new.next = self.top
            self.top = new
            self.min = value
        else:
            new = Node(value)
            new.next = self.top
            self.top = new

        print('number inserted {}'.format(value))


    def __repr__(self):
        out = []

        if self.top is None:
            return []
        cur = self.top
        while cur:
            out.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(out) + ']'

    def pop(self):
        if self.top is None:
            return print('stack is empty')

        else:
            removed_value = self.top.data
            self.top = self.top.next
            if removed_value < self.min:
                print('the poped value is {}'.format(self.min))
                self.min = (2*self.min) - removed_value

            else:
                print('the poped value is {}'.format(removed_value))



    def getMin(self):
        return print('Minimum Element in the stack is {}'.format(self.min))

    def peek(self):
        if self.top is None:
            return print('stack is empty')
        if self.top.data < self.min:
            return print('Top most element is {}'.format(self.min))
        else:
            return print('Top most element is {}'.format(self.top.data))

            
if __name__ == "__main__":
    #a = [1,2,1,3,2,3,1,1,3]
    #op: 3 2 1
    t = int(input('enter no of testcases'))
    for i in range(t):
        n = int(input('no of queries'))
        string = input('enter queries and values')
        inp = [int(e) for e in string.split()]
        val = 0
        s = Stack()
        while val < len(inp):
            if inp[val] == 1:
                s.push(inp[val+1])
                val +=2
            elif inp[val] == 2:
                s.pop()
                val +=1

            elif inp[val] == 3:
                s.getMin()
                val +=1
            else:
                s.peek()
                val +=1
                
                
        
