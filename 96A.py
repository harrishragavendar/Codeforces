s = input()
l = 0
cnt = 0
flag = False
for r in range(len(s)):
    if s[l] == s[r]:
        cnt += 1
        if cnt == 7:
            print("YES")
            flag = True
            break
    else:
        l = r
        cnt = 1
if not flag:
    print("NO")