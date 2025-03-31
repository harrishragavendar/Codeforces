n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
s = set(p).union(set(q))
if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")