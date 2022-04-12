class Stack:

    def __init__(self, list):
        self.stack = []
        for value in list:
            self.stack.append(value)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def output(self):
        print(self.stack)


class Queue:
    def __init__(self, list):
        self.queue = []
        for value in list:
            self.queue.append(value)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def output(self):
        print(self.queue)

if __name__=="__main__":
    s = Stack([1,2,3,4])
    s.output()
    s.push(9)
    s.output()
    s.pop()
    s.push(8)
    s.output()
    q = Queue(['pra', 'na', 'chai', 'pari'])
    q.enqueue('tej')
    q.output()
    q.dequeue()
    q.dequeue()
    q.output()
