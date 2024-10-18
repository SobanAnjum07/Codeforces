def sol(n ,t, books:list):
    
    max_books = 0
    total_time = 0
    i = 0
    
    for j in range(n):
        
        total_time += books[j]
        
        while total_time > t:
            total_time -= books[i]
            i += 1
            
        max_books = max(max_books, j - i + 1)
    
    return max_books
    

if __name__ =="__main__":
    
    n, t = map(int, input().split())
    books = list(map(int, input().split()))

    print(sol(n, t, books))
    