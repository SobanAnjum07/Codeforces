def sol(n, nums):
    

    i = 1
    start_flag = False
    while i < n:
        if nums[i-1] > nums[i]:
            start = i


        
    pass


if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))

    print (sol(n, nums))
