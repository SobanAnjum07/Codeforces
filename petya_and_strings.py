def main():
    str_a = input().lower()
    str_b = input().lower()
    if str_a < str_b:
        print(-1)
    elif str_a > str_b:
        print(1)
    else:
        print(0)
main()