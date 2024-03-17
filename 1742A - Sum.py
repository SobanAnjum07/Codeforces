
def check_sum(lst):
    max_ = max(lst)
    
    print("YES" if( lst[0] + lst[1] + lst[2] - max_ - max_ == 0) else "NO")
    

if __name__ == "__main__":
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        (check_sum(lst))