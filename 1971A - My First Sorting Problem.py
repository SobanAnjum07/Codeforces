import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        a, b = map(int, input().strip().split())
        
        if a < b:
            print(a, b)
        else:
            print(b, a)
        