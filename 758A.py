n = int(input())
arr = list(map(int, input().split()))
maxw = max(arr)
ans = 0
for a in arr:
    if a < maxw:
        ans += maxw - a
print(ans)