if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    div = 0
    for i in range(n):
        div += l[i] / 100
    print((div/ n) * 100 )