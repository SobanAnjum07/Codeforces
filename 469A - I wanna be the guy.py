if __name__ == '__main__':
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l = l1[1:] + l2[1:]
    s = set(l)
    if len(s) >= n and (n in s):
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')