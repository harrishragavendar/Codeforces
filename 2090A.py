t = int(input())
inputs = []
for i in range(t):
    inputs.append(list(map(int, input().split())))

for x, y, a in inputs:
    a += 0.5
    a = a % (x + y)
    curr = True
    while a >= 0:
        if curr:
            a -= x
            if a < 0: 
                print("NO")
                break
        else:
            a -= y
            if a < 0: 
                print("YES")
                break
        curr = not curr