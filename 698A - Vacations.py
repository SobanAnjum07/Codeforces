
def sol (n, activities):
    
    dp = [[float('inf')] * 3 for _ in range(n)]

    if activities[0] == 0:
        dp[0][0] = 1  
    elif activities[0] == 1:
        dp[0][1] = 0  
        dp[0][0] = 1  
    elif activities[0] == 2:
        dp[0][2] = 0  
        dp[0][0] = 1  
    elif activities[0] == 3:
        dp[0][1] = 0  
        dp[0][2] = 0  
        dp[0][0] = 1  

    for i in range(1, n):

        dp[i][0] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + 1  # Rest

        if activities[i] == 1 or activities[i] == 3:
            dp[i][1] = min(dp[i-1][0], dp[i-1][2])  # Contest

        if activities[i] == 2 or activities[i] == 3:
            dp[i][2] = min(dp[i-1][0], dp[i-1][1])  # Gym

    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

if __name__ == "__main__":
    
    n = int(input())  
    activities = list(map(int, input().split()))  
    print(sol(n, activities))