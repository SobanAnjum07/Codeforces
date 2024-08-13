def sol():
    
    n, s, m = map(int, input().split())
    lst = [[0, 0], [m, m]] + [list(map(int, input().split())) for i in range(n)]
 
    lst.sort()
 
    for i in range(1, n + 2):
 
        if lst[i][0] - lst[i - 1][1] >= s:
            return "YES"
        
    return "NO"
 
 
if __name__ == "__main__":
 
    for _ in range(int(input().strip())):
 
        print(sol())