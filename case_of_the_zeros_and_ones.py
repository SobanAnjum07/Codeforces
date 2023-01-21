def main():
    size = int(input())
    s = input()
    print( max(s.count('1'),s.count('0')) - min(s.count('1'),s.count('0')))
main()