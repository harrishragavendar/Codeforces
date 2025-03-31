# https://codeforces.com/problemset/problem/520/A
n=input()
s=input()
mask=[0]*26
for ch in s:
    ch = ord(ch)
    if 65 <= ch <= 90:
        mask[ch-65] += 1
    else:
        mask[ch-97] += 1
flag=False
for i in mask:
    if i == 0:
        print("NO")
        flag=True
        break
if not flag:
    print("YES")