if __name__ == '__main__':

    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        count = 0
        for ch in s:
            if ch == 'Q':
                count += 1
            elif count > 0:
                count -= 1
        if count <= 0: print('Yes')
        else: print('No')