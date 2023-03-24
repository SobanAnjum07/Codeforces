if __name__ == "__main__":
    strength, t = map(int,input().split())
    l = []
    for i in range(t):
        l.append(list(map(int,input().split())))
    l.sort()
    
    flag = "YES"
    for power in l:
        if strength > power[0]:
            strength+=power[1]
        else:
            flag ="NO"
            break
        
    print(flag)