def main():
    t = input()
    s = input()
    i = 0
    j = len(s)-1
    flag = True
    while i < len(t):
        if t[i] != s[j]:
            print('NO')
            flag = False
            break
        i += 1
        j -= 1
    if flag:
        print('YES')
main() 