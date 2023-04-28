def sol(nums):
    nums.sort()
    
    a, b = [], []
    
    chk = 0
    while len(nums):
        if chk % 2 == 0: 
            b.append(nums.pop())
        else: 
            a.append(nums.pop())
            if sum(a) != sum(b):
                if not len(nums): 
                    return "NO"
                else: 
                    a.append(nums.pop()) 
        
        chk  += 1
                
    
    return "YES" if sum(a) == sum(b) else "NO"
    
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        lst = [int(x) for x in input().split()]
        
        print (sol(lst))