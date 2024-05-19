import sys
input = sys.stdin.readline
from collections import Counter

def sol(n: int, s : str):
    
    if len(s) == 1: return s
    
    hash_map = Counter(s)
    ret_s = ""
    
    for k in hash_map:
        if hash_map[k] % n != 0:
            return -1

        ret_s += (k * (hash_map[k] // n ))
    
       
    return ret_s * n    
    

if __name__ == '__main__':
    
    
    n = int(input())
    s = input().strip()
    
    print(sol(n ,s))