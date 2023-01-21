def main():
    n , t= map(int, input().split())
    c = input()
    b = list(c)
    changed = ""
 
    while (t > 0):
        i = 0
        while i < (len(b)-1):
            if (b[i] == 'B' and b[i+1] == 'G'):
                b[i], b[i+1] = b[i+1], b[i]
                i += 1
            i += 1
        t -= 1
 
    for i in range(len(b)):
        changed += b[i]
 
    print(changed)
main()