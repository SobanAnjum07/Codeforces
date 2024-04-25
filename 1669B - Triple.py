from collections import defaultdict

def sol(lst):
    
    cnt = defaultdict(int)
    for ele in lst:
        
        cnt[ele] += 1
        if cnt[ele] == 3: return ele
    return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        
        n = int(input())
        lst = list(map(int, input().split()))
        print(sol(lst))