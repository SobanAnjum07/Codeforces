import sys
input = sys.stdin.readline

def sol(paren):
    
    prefix = 0
    dp = []
    i = 1
    for i,p in enumerate(paren):
        
        dp.append(([prefix, -i, paren[i]]))
        
        if p == "(":
            prefix += 1
        else:
            prefix -= 1
        
    
    # dp_sorted = sorted(dp, key= lambda x : (x[0], -x[1]))  
    dp.sort()
    print("".join(x[2] for x in dp))
    
    

if __name__ == "__main__":
    
    paren = input().strip()
    
    (sol(paren))
