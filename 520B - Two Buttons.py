def sol(n, m):
    
    steps = 0
    
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        steps += 1
        
    #! m <= n means we need n steps
    
    return steps + (n - m)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    
    print(sol(n, m))