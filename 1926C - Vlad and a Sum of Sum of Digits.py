import sys
input = sys.stdin.readline

def add(n):
    rem = 0;
    while n:
        rem += n % 10
        n //= 10    
    return rem


if __name__ == "__main__":
    
    N = 2 * 10**5 + 10
    dp = [0] * N
    
    for i in range(N):
        if i: dp[i] += dp[i-1];
        dp[i] += add(i)
    
    for _ in range(int(input())):
        n = int(input())
        print(dp[n])
            