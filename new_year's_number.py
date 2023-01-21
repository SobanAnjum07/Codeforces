def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        no = n // 2020
        target = n % 2020
        if n >= 2020:
            if target <= no:
                print('Yes')
            if target > no:
                print('No')
        else:
            print('No')
main()