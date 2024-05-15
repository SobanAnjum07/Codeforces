import sys
input = sys.stdin.readline
from collections import Counter


if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        check = Counter(s)
        if len(check.keys()) == 1:
            print("NO")
        else:
            print("YES")
            c = s[::-1]
            if c == s:
                c = s[-1] + s[:len(s)-1]
            print(c)
        
    
