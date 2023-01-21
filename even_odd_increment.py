def even_odd_increments(n, q, array, queries):
    even, odd = 0, 0
    seven, sodd = 0, 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            seven += array[i]
            even += 1
        else:
            sodd += array[i]
            odd += 1
    for query in queries:
#         print(even, odd, seven, sodd)
        evenodd = query[0]
        value = query[1]
        sum_ele = 0 
        if evenodd == 0:
            if value % 2 == 0:
                seven += (value * even)
            else:
                sodd += (seven + value * even)
                odd += even
                seven, even = 0, 0
        elif evenodd == 1:
            if value % 2 == 0:
                sodd += (value * odd)
            else:
                seven += (sodd + value * odd)
                even += odd
                sodd, odd = 0, 0
        print(seven+sodd)
        
        
t = int(input())
for i in range(t):
    n, q = input().split(" ")
    n, q = int(n), int(q)
    array = input().split(" ")
    array = [int(val) for val in array]
    queries = []
    for i in range(q):
        query = input().split(" ")
        query = [int(val) for val in query]
        queries.append(query) # [0, 1]
    even_odd_increments(n, q, array, queries)