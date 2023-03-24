if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    max = 1
    count = 1
    for i in range(1, n):
        if a[i] >= a[i-1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    print(max)