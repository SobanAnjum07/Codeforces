def main():
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for num in arr:
        if num <= h:
            sum += 1
        else:
            sum += 2
    print(sum)
main() 