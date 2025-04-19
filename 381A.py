n = int(input())
arr = list(map(int, input().split()))
l = 0
r = n - 1
a = b = 0
curr = 'a'
for _ in range(n):
    if curr == 'a':
        if arr[l] > arr[r]:
            a += arr[l]
            l += 1
        else:
            a += arr[r]
            r -= 1
        curr = 'b'
    else:
        if arr[l] > arr[r]:
            b += arr[l]
            l += 1
        else:
            b += arr[r]
            r -= 1
        curr = 'a'
print(a, b)