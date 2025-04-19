n = int(input())
arr = list(map(int, input().split()))
odds = evens = 0
for i in range(3):
    if arr[i] & 1 == 0:
        evens += 1
    else:
        odds += 1
if odds >= 2:
    for i in range(len(arr)):
        if arr[i] & 1 == 0:
            print(i + 1)
            break
else:
    for i in range(len(arr)):
        if arr[i] & 1 == 1:
            print(i + 1)
            break