if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    tram = b
    max_cap = b
    for i in range(n-1):
        a, b = map(int, input().split())
        tram -= a
        tram += b
        if max_cap < tram :
            max_cap = tram       
 
    print(max_cap)