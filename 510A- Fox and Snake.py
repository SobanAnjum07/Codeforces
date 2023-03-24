def fox_and_snake(n, m):
    for i in range(n):
        
        if i % 2 == 0:
            print('#' * m)
            
        elif i % 4 == 1:
            print('.' * (m - 1) + '#')
            
        else:
            print('#' + '.' * (m - 1))
            
if __name__ == '__main__':
    n, m = map(int, input().split())
    fox_and_snake(n, m)
