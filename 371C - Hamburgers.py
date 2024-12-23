def can_make(mid,recipe, stonk, prices, money):

    total_cost = 0
    
    for i in range(3):  # Bread, sausage, cheese
        needed = max(0, mid * recipe[i] - stonk[i])  # Shortfall
        total_cost += needed * prices[i]  # Cost for shortfall
    
    return total_cost <= money


def max_hamburgers(recipe_str, stonk, prices, money):
    
    recipe = [recipe_str.count('B'), recipe_str.count('S'), recipe_str.count('C')]
    
    l = 0 ; r = 10**13
    ans = 0
    
    while l <= r:
        mid = (l+r) // 2
        print(mid)
        if can_make(mid, recipe , stonk, prices, money):
            ans = mid
            l = mid + 1
            
        else:
            r = mid - 1
            
    return ans
    


recipe_str = input().strip() 
n_b, n_s, n_c = map(int, input().split())  
p_b, p_s, p_c = map(int, input().split())  
money = int(input())  

result = max_hamburgers(recipe_str, [n_b, n_s, n_c], [p_b, p_s, p_c], money)
print(result)