if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int,input().split())
        print((b - a % b) % b)