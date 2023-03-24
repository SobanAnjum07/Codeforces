if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        if len(s)%2 == 0:
            if s[0:len(s)//2] == s[len(s)//2:]: print('YES')
            else:   print('NO')
        else:
            print('NO')