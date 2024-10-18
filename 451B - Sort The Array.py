def sol(n, nums):
    
    i = 0
    flag = False
    run_flag = False
    
    for i in range(n-1):
        
        if nums[i] > nums[i+1] and not flag : #means flag is flase
            flag = True
            run_flag = True
            left_index = i
            
        elif flag and nums[i] < nums[i+1]:
            flag = False
            right_index = i
            break
        
    
    if run_flag and flag:
        right_index = n-1
        
    if run_flag:
        
        split = nums[left_index:right_index+1]
        
        if len(split) == n:
            check = split[::-1]
        elif left_index == 0:
            check = split[::-1] + nums[right_index+1:n]
        elif right_index == n-1:
            check =  nums[0:left_index] + split[::-1]
        else:
            check = nums[0:left_index] + split[::-1] + nums[right_index+1:n]
            
                    
        for i in range(n-1):
            
            if check[i] > check[i+1]:
                print("no")
                return
                        
        print("yes")
        print(f"{left_index+1} {right_index+1}")
        return
    else:
        print("yes")
        print("1 1")
        

if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))

    (sol(n, nums))
