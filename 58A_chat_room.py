if __name__ == '__main__':
    s = input()
    em_s  = ''
    for i in range(len(s)):
        if em_s == '':
            if s[i] == 'h':
                em_s += 'h'
 
        elif em_s =='h':
            if s[i] == 'e':
                em_s += 'e'
 
        elif em_s =='he':
            if s[i] == 'l':
                em_s += 'l'
 
        elif em_s =='hel':
            if s[i] == 'l':
                em_s += 'l'
 
        elif em_s =='hell':
            if s[i] == 'o':
                em_s += 'o'
                break
    if em_s == 'hello':
        print('YES')
    else:
        print('NO')