#implement queue using two stacks
# implement enque strictly
class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())


    def dequeue(self):
        if len(self.s1) == 0:
            return print('Queue is empty')

        x = self.s1.pop()
        return x


class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if len(self.s1) == 0:
            return print('Q is empty')

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        x = self.s2.pop()

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

        return x
    

    


if __name__ == "__main__":
    Q = Queue2()
    Q.enqueue('a')
    Q.enqueue('b')
    Q.enqueue('c')
    Q.enqueue('d')
    print(Q.dequeue())
    print(Q.dequeue())
    
        
