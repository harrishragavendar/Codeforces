n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
s = set(p[1:]).union(set(q[1:]))
if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")