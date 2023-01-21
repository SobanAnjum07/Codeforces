def main():
    n1 = input()
    n2 = input()
    s = ''
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            s+= '0'
        else:
            s+= '1'
    print(s)
main()