def helper(col_sum, return_arr, i, j):
    
    if return_arr[j][i] == "o":
        j -=1
    while j >= 0 and col_sum > 0:
        return_arr[j][i] = "*"
        col_sum -= 1
        j -= 1
        
    return col_sum, return_arr
        
def sol(fall, rows, cols):
    return_arr = [["." for i in range(cols)] for j in range(rows)]
    
    for i in range(cols):
        col_sum = 0
        
        for j in range(rows):
            if fall[j][i] == "*":
                col_sum +=1
            elif fall[j][i] == 'o':
                return_arr[j][i] = 'o'
                col_sum, return_arr =  helper(col_sum, return_arr, i, j)

        col_sum, return_arr =  helper(col_sum, return_arr, i, j)
        
        
    for hehe in return_arr:
        print(*hehe, sep="")
if __name__ == "__main__":
    
    for _ in range(int(input())):
        fall = []
        
        rows, cols = map(int , input().split())
        for _ in range(rows):
            s = list(input())
            fall.append(s)
        sol(fall, rows, cols)
        
        