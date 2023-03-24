if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l.reverse()
    s = 0
    count = 0
    for i in range(n):
        s += l[i]
        g = sum(l[i+1:])
        count += 1
        if s > g:
            print(count)
            break
    print()