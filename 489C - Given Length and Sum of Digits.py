def sol(m:int, s:int):
    
    if (s == 0 and m > 1) or (s > 9 * m): return -1, -1
    
    #! largest
    
    remaining_sum = s ; largest = ""
    
    for i in range(m):
        
        digit = min(9, remaining_sum)
        largest += str(digit)
        remaining_sum -= digit
        
    
    #! smallest
    
    remaining_sum = s
    smallest = ["0"] * m ; smallest[0] = 1
    remaining_sum -= 1
    
    for i in range(m-1, 0 ,-1):
        
        if remaining_sum > 0:
            
            digit = min(9, remaining_sum)
            remaining_sum -= int(digit)
            smallest[i] = str(digit)
            
            
    smallest[0] = str(int(smallest[0]) + remaining_sum)
    
    return int("".join(smallest)) , int(largest)


if __name__ == "__main__":
    
    m, s = map(int, input().strip().split())
    print(*sol(m,s))
    