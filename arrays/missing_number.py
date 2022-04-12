#findout the missing number in the array

def find_missing(ar):
    n = len(ar)+1
    natural_sum = (n*(n+1))//2
    print(natural_sum)
    print(sum(ar))
    print(natural_sum-sum(ar))
        
        
        


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40]
#find_missing(a)
 #= [1,2,3,5]
find_missing(a)
