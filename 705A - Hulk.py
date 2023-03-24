if __name__ == '__main__':
 
    n = int(input())
    s = ''
    s1 ='I hate'
    s0 = "I love"
    for i in range(1, n):
        if i%2 == 1:
            s += s1
            
        else:
            s+= s0
        s+= ' that '
    if n%2 == 0:
        s += s0 + ' it'
    else:
        s += s1 + ' it'
    print(s)