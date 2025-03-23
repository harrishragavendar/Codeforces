x = 0
n = int(input())
for _ in range(n):
    op = input()
    if '+' in op: x += 1
    else: x -= 1
print(x)