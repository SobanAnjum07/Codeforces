import sys
input = sys.stdin.readline
from collections import defaultdict

if __name__ == "__main__":
    
    winner = defaultdict(int)
    
    for _ in range(int(input())):
        
        s = input().strip()
        winner[s] += 1
        
    val = [x for x in winner]
    
    if len(val) == 1:
        
        print(val[0])
    else:
        
        print(val[0] if winner[val[0]] > winner[val[1]] else val[1])
