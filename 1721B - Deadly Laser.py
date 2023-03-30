for _ in range(int(input())):
    n, m, x, y, d = map(int, input().split())
    if (x-1 > d and m-y > d) or (y-1 > d and n-x > d):
        print(n+m-2)
    else:
        print(-1)
