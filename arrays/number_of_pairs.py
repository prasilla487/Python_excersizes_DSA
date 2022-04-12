# pairs which follow x power y and y power x
# x = [2,1,6] y = [1,5]
#output : 3 2^1 > 1^2 , 2^5>5^2 , 6^1>1^6

def count_pairs(x, y):
    count = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if i ** j > j ** i:
                count +=1
    print(count)

if __name__ == "__main__":
    t = input('enter testcases')
    for i in range(int(t)):
        m = input("enter sizes")
        n = input("enter sizes")
        inp = input("enter elements")
        x = [int(e) for e in inp.split()]
        inp = input("enter elements of y")
        y = [ int(e) for e in inp.split()]
        count_pairs(x,y)
