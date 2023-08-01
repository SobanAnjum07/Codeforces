def isSort(lst):
    
    lst1= lst.copy();
    lst.sort()
    if lst1 != lst:
        return True
    return False

def sol(n, lst):
    
    if isSort(lst): return 0
    min_ = 9999999999999
    
    for i in range(n-1):
        temp = abs(lst[i] - lst[i+1]);
        if temp < min_: 
            min_ = temp;
    return min_ //2 +1
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        
        n = int(input());
        lst = list(map(int, input().split()));
        print(sol(n, lst));
        
        
