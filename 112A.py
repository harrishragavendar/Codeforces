s1 = input().lower()
s2 = input().lower()
i = 0
printed = False
while i < len(s1):
    if s1[i] != s2[i]:
        if s1[i] > s2[i]:
            print(1)
        else:
            print(-1)
        printed = True
        break
    i += 1
if not printed:
    print(0)