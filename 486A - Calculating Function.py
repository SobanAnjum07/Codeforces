if __name__ == '__main__':
    n = int(input())
    
    if n%2 == 0:
        ans = n/2
    else: 
        ans = ((n+1)/2) * (-1)
    print(int(ans))
    
    # (Simple Solution)
    # sum = 0
    # for i in range(1,n+1):
    #     if i%2 == 1:
    #         sum-= i
    #     else:
    #         sum += i
    # print(sum)
    
