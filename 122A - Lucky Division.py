def lucky_division(n):
    lucky = [4, 7, 47, 74, 447, 474, 477, 744, 747, 774]
    for i in lucky:
        if n % i == 0:
            return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    print(lucky_division(n))
        