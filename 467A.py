n = int(input())
ans = 0
for _ in range(n):
    p, q = list(map(int, input().split()))
    if q - p >= 2:
        ans += 1
print(ans)