n=int(input())
for _ in range(n):
    a,b,c = list(map(int, input().split()))
    if (a + b == c) or (a + c == b) or (b + c == a):
        print("YES")
    else:
        print("NO")