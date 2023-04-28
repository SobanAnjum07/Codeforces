if __name__ == '__main__':
    s = 0
    n = int(input())
    dgnl = 0
    sec_dgnl= n -1
    mid_col = int((((n-1)/2)))
    for i in range(n):
        
        l = list(map(int, input().split()))
        
        if i == ((n-1)/2):
            hehe = sum(l)
        else:
            s += l[dgnl] + l[sec_dgnl] + l[mid_col]
        
        dgnl += 1
        sec_dgnl -= 1
    s += hehe
    print(s)