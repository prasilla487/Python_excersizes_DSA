#triplets [1,2,3,4] ans = (1,2,3) (1,3,4) so 2
def count_triplets(a, n):
    max_val = 0
    for i in range(n):
        max_val = max(max_val, a[i])

    freq = [0]*(max_val+1)
    for i in range(n):
        freq[a[i]] +=1

    print(freq)
    ans = 0
    #case 0 : 0,0,0
    ans += (freq[0]*(freq[0]-1)*(freq[0]-2)//6)
    print(ans)
    print('--')

    #case 1: 0,x,x
    for i in range(1,max_val+1):
        ans += (freq[0]*(freq[i]-1)*freq[i]//2)
    print(ans)
    print('--')
    #case 2: x,x,2x
    for i in range(1,max_val-2):
        ans += (freq[i]-1)*freq[i]//2*freq[2*i]
    print(ans)
    print('---')
    #case 3: x, y, x+y
    for i in range(1,max_val+1):
        for j in range(i+1,max_val-i+1):
            ans += freq[i]*freq[j]*freq[i+j]
    
    return ans

if __name__ == "__main__":
    a = [1,5,2,3]
    n = len(a)
    print(count_triplets(a, n))
