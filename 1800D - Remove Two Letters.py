import sys
from collections import defaultdict
input = sys.stdin.readline


#  -> this will give memory error (a naive approach)
# def sol1(s,n):
#     i=0; j=1
#     hash_map = defaultdict(int)
    
#     while j < len(s):
#         ap = s[:i] + s[j+1:]
        
#         if hash_map[ap] == 0:
#             hash_map[ap] = 1
        
#         i+=1; j+=1
        
#     val = hash_map.values()
#     return sum(val)


def sol(n, s):
    sum_  = 0
    i = 0
    while i <= n-2:
        if i == n-2: sum_ += 1 ; break;
        if s[i] != s[i + 2]:
            sum_ += 1
        
        i += 1
    return sum_
            
if __name__ == "__main__":
    
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        
        print(sol(n, s))
    

    