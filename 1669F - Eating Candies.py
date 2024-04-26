def sol(weights: list, n:int):
    
    pre_sum = 0
    left_sum_lst = []
    
    for i in range(n):
        pre_sum += weights[i]
        left_sum_lst.append(pre_sum)
        
    right_pre_sum = 0
    right_sum_lst = [0] * n
    for i in range(n-1, -1, -1):
        right_pre_sum += weights[i]
        right_sum_lst[i] = (right_pre_sum)
    
    r = n-1
    l = 0
    max_= 0
    
    while l < r:
        if left_sum_lst[l] < right_sum_lst[r]:
            l += 1
        
        elif left_sum_lst[l] > right_sum_lst[r]:
            r -= 1
            
        else:
            max_ = (l + 1) + (n -r)
            l += 1
            r -= 1
    
    print(max_)

if __name__ == "__main__":
    
    for _ in range(int(input())):
        
        n = int(input())
        weights = list(map(int, input().split()))
        (sol(weights, n))