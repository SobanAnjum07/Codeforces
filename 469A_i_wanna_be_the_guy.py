def i_became_the_guy(n, l1, l2):
    l = l1 + l2
    s = set(l)
    if len(s) >= n and (n in s):
        return 'I become the guy.'
    else:
        return 'Oh, my keyboard!'
        
if __name__ == '__main__':
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    print(i_became_the_guy(n, l1, l2))