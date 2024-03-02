def main():
    x = int(input())
    if x % 5 != 0:
        num = (x//5) + 1
    else:
        num = (x/5)
    print(int(num))
main() 