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

def sol(n:int , k:int) -> int:
    check = (k-1) // (n-1)
    return k + check
    
    

if __name__ == "__main__":
    
    for _ in range(int(input())):
        n , k = map(int, input().strip().split())
        
        print(sol(n, k))
    

    