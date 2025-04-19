ins=set(input())
valid={'H', 'Q', '9'}
flag=False
for v in valid:
    if v in ins:
        print("YES")
        flag=True
        break
if not flag:
    print("NO")