def main():
    upper = 0
    lower = 0
    s = input()
    for i in range(len(s)):
        if s[i].isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        print(s.upper())
    elif upper <= lower:
        print(s.lower())
main()