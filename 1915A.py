n = int(input())
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)