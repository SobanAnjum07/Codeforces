# unoptimized approach
# def sol(n: int, k: int , lst: list):
#     left = 0
#     right = len(lst)-1
#     l_t = True
#     r_t = False
#     zero = 0
#     while k:
        
#         if l_t:
            
#             lst[left] -= 1
#             if lst[left] == 0:
#                 zero += 1
#                 if zero == len(lst) : break;
#                 left += 1
#             l_t = False
#             # r_t = True
        
#         else:
            
#             lst[right] -= 1
#             if lst[right] == 0:
#                 zero += 1
#                 if zero == len(lst) : break;
#                 right -= 1
#             # r_t = False
#             l_t = True
        
#         k -= 1
        
#     return lst.count(0)
            
#? optimized approach (accepted)
def sol(n: int, k: int , lst: list):
    if sum(lst) <= k: return n
    
    if k % 2 == 0:
        left = k//2
        right = k //2
    else:
        left = k//2 + 1
        right = k //2
    
    ind = 0
    pre_sum = 0
    
    for ele in lst:
        pre_sum += ele
        if pre_sum > left:
            break
        ind += 1
        
    pre_sum = 0
    for i in range(len(lst)-1, -1, -1):
        pre_sum += lst[i]
        if pre_sum > right:
            break
        ind += 1
        
    return ind
        
        

if __name__ == "__main__":
    
    for _ in range(int(input())):
        n, k = map(int , input().split())
        lst = list(map(int, input().split()))
        
        print(sol(n, k, lst))