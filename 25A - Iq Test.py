def sol(lst):
    eve = []
    odd = []
    for ele in lst:
        if ele %2 == 0:
            eve.append(ele)
        else:
            odd.append(ele)
            
    if len(eve) == 1: check = eve[0];
    else: check = odd[0];
    
    return lst.index(check) + 1
 
if __name__ == '__main__':
    
    
    n = int(input())
    lst = list(map(int, input().split()))
    print(sol(lst))