def main():
    n = input()
    flag = 'No'
    for i in range(len(n)-6):
        if n[i:i+7] == '0000000':
            print("YES")
            flag = 'Yes'
            break
        elif n[i:i+7] == '1111111':
            print("YES")
            flag = 'Yes'
            break
    if flag != 'Yes':
        print("NO")
main()