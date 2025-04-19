n = int(input())
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > a and b < c) or (b > c and b < a):
        print(b)
    else:
        print(c)