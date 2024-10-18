def sol(n ,t, books:list):
    
    books.sort()
    
    l , r = 0 , n
    max_len = 0
    
    while l<r:
        current_sum = sum(books[l:r])
        
        if current_sum > 
    pass

if __name__ =="__main__":
    
    n, t = map(int, input().split())
    books = list(map(int, input().split()))

    print(sol(n, t, books))
    