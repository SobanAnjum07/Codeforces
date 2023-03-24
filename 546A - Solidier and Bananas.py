def main():
    k, n, w = map(int, input().split())
    i = 1
    sum = 0
    while i <= w:
        sum += i * k
        i += 1
    req = sum - n
    if req > 0:
        print(req)
    else:
        print(0)
main()