#given array of integers representing cost of stock, find out in which day to buy
#and which day to sell so that willget max profit
# ex a = [100,160,210,360,40,53,696] op: (0,3) (4,6) (buy_day, sell_day)
0
def stock(ar):
    n = len(ar)
    max_num = -1235
    start = 0
    for i in range(n):
        if max_num < ar[i]:
            max_num = ar[i]

        

a = [100,50,30,20]
stock(a)
            
