def main():
    a = input()
    l = []
    s = ''
    for i in range(len(a)):
        if ord(a[i]) >= ord('0') and ord(a[i]) <= ord('9'):
            l.append(int(a[i]))
    l.sort()
    for num in l:
        s += str(num) + '+'
    print(s[0:-1])
main()