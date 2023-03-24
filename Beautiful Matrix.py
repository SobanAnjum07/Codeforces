def main():
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l3 = list(map(int, input().split()))
    l4 = list(map(int, input().split()))
    l5 = list(map(int, input().split()))
    lst = [l1, l2, l3, l4, l5]
    index_x, index_y = 0, 0
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == 1:
                index_x = i
                index_y = j
 
    if index_x != 2:
        if index_x < 2:
            while index_x != 2:
                index_x += 1
                count += 1
        elif index_x > 2:
            while index_x != 2:
                index_x -= 1
                count += 1
 
    if index_y != 2:
        if index_y < 2:
            while index_y != 2:
                index_y += 1
                count += 1
        elif index_y > 2:
            while index_y != 2:
                index_y -= 1
                count += 1
    print(count)

#there is also an alternative version of the code that is just an algo(maths eq)
# will be added soon
 
main()