def check(s):
    for chr in s:
        if chr == "H" or chr == 'Q' or chr == '9':
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    s = input()
    print(check(s))
    