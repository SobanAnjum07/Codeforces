import sys
input = sys.stdin.readline
def sol(a, b):
    buffer = set(a)
    counter = len(a)
    for char in b:
        if char not in buffer:
            counter += 1

    return counter


if __name__ == "__main__":

    for _ in range(int(input().strip())):
        a = list(input().strip())
        b = list(input().strip())

        print(sol(a,b))
