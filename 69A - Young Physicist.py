if __name__ == '__main__':
    n = int(input())
    final_sum =  0
    
    a = 0
    b = 0
    c = 0
    
    for _ in range(n):
        
        lst = list(map(int, input().split()));

        a += lst[0]
        b += lst[1]
        c += lst[2]
        
    if a ==0 and b == 0 and c ==0: print('YES');
    else: print('NO')