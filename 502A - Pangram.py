def pangram(s):
    s = s.lower()
    for i in range(97,123):
        if chr(i) not in s:
            return "NO"
    return 'YES'

if __name__ == '__main__':

    n = int(input())
    s = input()
    if n < 26:
        print("NO")
    
    else:
        print(pangram(s))
        