def main():
    n = int(input())
    g = 0
    if n > 0:
        s = input()
        check_prev = s
        g = 1
        for i in range(n-1):
            s = input()
            if check_prev == s:
                pass
            else:
                g += 1
                check_prev = s
    print(g)
main()