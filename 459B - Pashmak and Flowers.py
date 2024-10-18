def sol(n, arr:list):

    min_el = min(arr)
    max_el = max(arr)
    
    min_count = arr.count(min_el)
    max_count = arr.count(max_el)
    
    max_beauty = max_el - min_el
    
    if min_el == max_el: #if all the elements are same
        count =  (n * (n-1)) // 2 #combination formula 
        
    else:
        count = min_count * max_count
        
    return max_beauty, count

if __name__ == "__main__":
    
    n = int(input())
    flowers = list(map(int, input().split()))
    
    print(*sol(n, flowers))