
#  a as a substring and b as a subsequence.
def sol(a, b):

    x = len(a)
    y = len(b)
    ans = x + y
    for i in range(y):
        j = i
        for c in a:
            if j < y and c == b[j]:
                j += 1
        ans = min(ans, x + y - (j - i))
    return (ans)


if __name__ == "__main__":
    for _ in range(int(input().strip())):
        a = input()
        b = input()

        print(sol(a, b))
