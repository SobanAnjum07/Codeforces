import sys
input = sys.stdin.readline

def sol(n):
    dp = [1] * n

    for i in range(1, n):
        
        if lst[i] > lst[i -1]:
            dp[i] += dp[i-1]
        
    return max(dp)

if __name__ == '__main__':
    
    
    n = int(input())
    lst = list(map(int, input().split()))
    print(sol(n))