def beautiful_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year

if __name__ == '__main__':
    n = int(input())
    print(beautiful_year(n))
        