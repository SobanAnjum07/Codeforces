


def sol(lst, n):
    return sum(lst) - (min(lst) * n)

if __name__ == "__main__":
    
    for _ in range(int(input())):
        n = int(input())
        lst = list(map(int, input().split()))
        print(sol(lst, n))