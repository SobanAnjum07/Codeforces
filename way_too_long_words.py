def main():
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) > 10:
            new_s = s[0] + str(len(s[1:-1])) + s[-1]
            print(new_s)
        else:
            print(s)
main()