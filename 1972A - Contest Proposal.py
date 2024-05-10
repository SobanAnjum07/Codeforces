import sys
input = sys.stdin.readline

def sol1(n, lst1, lst2):
    pointer1 = 0
    pointer2 = 0
    indeces = 0
    while (pointer1 < n) and (pointer2 < n) :
        if lst1[pointer1] > lst2[pointer2]:
            indeces += 1
            pointer2 += 1
        else:
            pointer1 += 1 
            pointer2 += 1



    return indeces
if __name__ == "__main__":
    
    for _ in range(int(input())):
        n = int(input())
        lst1 = list(map(int, input().strip().split()))
        lst2 = list(map(int, input().strip().split()))
        
        print(sol1(n, lst1, lst2))