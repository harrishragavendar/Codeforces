n = int(input())
arr = list(map(int, input().split()))

prev_max = prev_min = arr[0]
amazing = 0

for i in range(1, len(arr)):
    if arr[i] > prev_max:
        prev_max = arr[i]
        amazing += 1
    if arr[i] < prev_min:
        prev_min = arr[i]
        amazing += 1

print(amazing)