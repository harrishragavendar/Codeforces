n = input()
arr = list(map(int, input().split()))
res = curr = 1
for r in range(1, len(arr)):
    if arr[r] >= arr[r-1]:
        curr += 1
    else:
        res = max(res, curr)
        curr = 1
res = max(res, curr)
print(res)