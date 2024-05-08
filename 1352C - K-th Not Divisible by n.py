import sys
input = sys.stdin.readline

def sol(n:int , k:int) -> int:
    check = (k-1) // (n-1)
    return k + check
     

if __name__ == "__main__":
    
    for _ in range(int(input())):
        n , k = map(int, input().strip().split())
        
        print(sol(n, k))
    

    