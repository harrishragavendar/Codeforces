n = int(input())
x = y = z = 0
for _ in range(n):
    _x, _y, _z = list(map(int, input().split()))
    x, y, z = x + _x, y + +y, z + _z
if x == y == z == 0:
    print("YES")
else:
    print("NO")