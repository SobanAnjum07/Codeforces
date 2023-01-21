def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        count = 0
        sum_a = sum(a)
        sum_b = sum(b)
        if a == b:
            print(count)
        else:
            if sum(a) == sum(b):
                count += 1
            elif sum(a) > sum(b):
                for i in range(n):
                    if a[i] != b[i] and a[i] == 1:
                        a[i] = 1 - a[i]
                        count+= 1
                    if a == b:
                        break
                    if sum(a) == sum(b):
                        count+= 1
                        break
                        
            elif sum_a < sum_b:
                for i in range(n):
                    if a[i] == 0 and (a[i] != b[i]):
                        a[i] = 1 + a[i]
                        count+= 1
                    if a == b:
                        break
                    if sum(a) == sum(b):
                        count+= 1
                        break
            print(count)
 
main()