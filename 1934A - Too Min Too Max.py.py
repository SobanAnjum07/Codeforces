# import math
def sol(n, a):
    # |𝑎𝑖−𝑎𝑗|+|𝑎𝑗−𝑎𝑘|+|𝑎𝑘−𝑎𝑙|+|𝑎𝑙−𝑎𝑖|
    i , j , k, l = 0, -1, 1, -2
    a.sort()
    max_ = (abs(a[i] - a[j]) + abs(a[j] -a[k]) + abs(a[k] - a[l]) + abs(a[l] - a[i]))

    
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             for l in range(n):
                    
    #                 if i!=j and  i!= k and i != l and j != k and j != l and k != l:
    #                     evalu = (abs(a[i] - a[j]) + abs(a[j] -a[k]) + abs(a[k] - a[l]) + abs(a[l] - a[i]))
    #                     if  max_ < evalu:
    #                         max_ = evalu
    return max_                        

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        lst = list(map(int, input().split()))
        
        
        print(sol(n,lst))