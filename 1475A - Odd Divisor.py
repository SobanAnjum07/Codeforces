import sys
input = sys.stdin.readline
 
 
def sol(n):
    
    if n & (n - 1) :
        return "YES"
    return "NO"
 
if __name__ == "__main__":
    
    
    for _ in range(int(input())):
        
        n = int(input())
        print(sol(n))