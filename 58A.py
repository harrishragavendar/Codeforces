word = input()
msg = ['h', 'e', 'l', 'l', 'o']
i = j = 0
for j in range(len(word)):
    if word[j] == msg[i]:
        i += 1
        if i == 5:
            print("YES")
            break
if i < 5:
    print("NO")