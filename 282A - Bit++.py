def main():
    n = int(input())
    sum = 0
    for i in range(n):
        s = input()
        if '+' in s:
            sum += 1
        elif '-' in s:
            sum -= 1
    print(sum)
main()