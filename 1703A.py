# https://codeforces.com/problemset/problem/1703/A
yes=set(["yes", "yeS", "yEs", "yES", "Yes", "YeS", "YEs", "YES"])
t=int(input())
for _ in range(t):
    s=input()
    if s in yes:
        print("YES")
    else:
        print("NO")