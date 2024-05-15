import sys
input = sys.stdin.readline

import bisect

def sol(m):
    return bisect.bisect_right(prices, m)

if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    prices.sort()
    for _ in range(int(input())):
        m = int(input())
        print(sol(m))
        
    