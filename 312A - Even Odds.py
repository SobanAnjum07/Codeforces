def sol(n, index):

    if n%2 == 0:
        if index <= n//2:
            return (index*2)-1
        else:
            return 2 *(index -n//2)
    else:
        if index <=(n//2+1):
            return 2 *(index-1)+1
        else:
            return 2 *(index -((n//2)+1))
        
if __name__ == "__main__":
    
    n, index = map(int, input().split())
    print(sol(n ,index))