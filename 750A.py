n, k = list(map(int, input().split()))
available_mins = 240 - k
probs = 0
for i in range(1, n+1):
    curr = 5 * i
    if available_mins - curr >= 0:
        available_mins -= curr
        probs += 1
    else:
        break
print(probs)