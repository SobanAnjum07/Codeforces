import sys
input = sys.stdin.readline
from collections import defaultdict

def sol(n:int, lst:list) -> int:
    prev = lst[0]
    prev1 = lst[1]
    
    hash_map = defaultdict(int)
    
    for ele in lst:
        hash_map[ele] += 1
        
    val = hash_map.values()
    print(val)
    return lst.index(min(hash_map[val[0]], hash_map[val[1]]))
        