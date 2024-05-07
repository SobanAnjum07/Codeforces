

import sys
from collections import defaultdict
input = sys.stdin.readline



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
def sol1(s,n):
    i=0; j=1
    hash_map = defaultdict(int)
    
    while j < len(s):
        ap = s[:i] + s[j+1:]
        
        if hash_map[ap] == 0:
            hash_map = 1
        
        i+=1; j+=1
        
    val = hash_map.values()
    return sum(val)

    
if __name__ == "__main__":
    
    for _ in range(int(input())):
        n = int(input())
        s = input()
        
        print(sol1(s ,n))
    

    