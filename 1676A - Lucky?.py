
def sol(s):
    
    if sum(s[0:3]) == sum(s[3:6]):
        return "YES"
    return "NO"

if __name__ == "__main__":
    for _ in range(int(input())):
        
        s = list(input())
        int_s = [int(ele) for ele in s]
        print(sol(int_s))