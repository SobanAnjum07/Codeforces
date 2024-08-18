def sol(n):
   
    mod_num = n // 4
    remainder = n % 4

    return (mod_num + remainder//2)

    
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input()) 
        print(sol(n))
