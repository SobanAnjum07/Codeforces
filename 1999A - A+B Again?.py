def sol(n):
 
    lst = [int(num) for num in n]
    return sum(lst)
 
 
 
if __name__ == "__main__":
 
    for _ in range(int(input().strip())):
        n = input()
        print(sol(n))