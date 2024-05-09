


# 5 r
#! rggry
# ? [0, 3] [1, 2]


"""def sol(s:str, n:int, c:str):
    index_ele  = [index for index, char in enumerate(s) if char == c]
    index_green = [index for index, char in enumerate(s) if char == "g"]
    
    if index_green[-1] > index_ele[0]:
        return index_green[-1] - index_ele[0] + 1
    else:
        return (index_green[-1] + 1) - (index_ele[0]+1)
"""

import sys
from collections import defaultdict
input = sys.stdin.readline




def sol(n:int, lst:list) -> int:
    prev = lst[0]
    prev1 = lst[1]
    
    hash_map = defaultdict(int)
    
    for ele in lst:
        hash_map[ele] += 1
        
    val = hash_map.values()
    print(val)
    return lst.index(min(hash_map[val[0]], hash_map[val[1]]))
        
        
    
if __name__ == "__main__":
    
    for _ in range(int(input())):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        
        print(sol(n, lst))
    

    