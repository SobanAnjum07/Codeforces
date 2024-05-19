import sys
input = sys.stdin.readline

def sol(n:int):
    
    q = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    
    lent = len(q)
    i = 1  

    # 1 2 4 8 
    while lent * i < n  :
        
        n -= lent * i
        i *= 2 # multiple of 2

    ind = (n - 1) // i
    return q[ind]

        

if __name__ == '__main__':
    
    
    n = int(input())
    print(sol(n))