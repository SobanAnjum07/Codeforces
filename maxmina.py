def main():
    t = int(input())
    for i in range(t):
        x, y = map(int,input().split())
        l = list(map(int, input().split()))
        count = 0
        for num in l:
            if num == 1:
                count += 1
        if count >=1:
            print("YES")
        else:
            print('NO')
main()