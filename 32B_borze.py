def main():
    n = input()
    s = ''
    i = 0
    while i < len(n):
        if n[i] == '.':
            s += '0'
            i += 1
        elif n[i] == '-':
            if n[i+1] == '.':
                s+= '1'
            else:
                s+= '2'
            i += 2
    print(s)
main()