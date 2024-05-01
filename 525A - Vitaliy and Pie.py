
from collections import defaultdict

def sol(n:int, s:str):
    dic = defaultdict(int)
    count = 0
    for i in range(len(s)):
        if s[i].islower():
            dic[s[i]] += 1
            
        else:
            dic[s[i].lower()] -= 1
            if dic[s[i].lower()] == -1:
                count += 1
                dic[s[i].lower()] += 1
      
    return count



if __name__ == "__main__":
    
    n = int(input())
    s = input().strip()
    
    print(sol(n , s))