#find the first position from where a truck will be able to complete the circle
class PetrolPump:
    def __init__(self, amount, dist):
        self.amount = amount
        self.dist = dist


def printTour(ar):
    n = len(ar)

    start = 0
    end = 1

    cur_petrol = ar[start].amount - ar[start].dist

    while start != end or cur_petrol < 0:

        while start != end and cur_petrol < 0:

            cur_petrol -= ar[start].amount - ar[start].dist

            start = (start +1 )%n

            if start == 0:
                return -1

        cur_petrol += ar[end].amount - ar[end].dist

        end = (end +1 ) %n

    return start



arr = [PetrolPump(4,6), PetrolPump(6,5), PetrolPump(7,3), PetrolPump(4,5)] 
start = printTour(arr) 
  
print("No solution" if start == -1 else "start =", start )
