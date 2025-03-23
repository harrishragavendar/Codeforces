word = input()
upper = lower = 0
for ch in word:
    if 65 <= ord(ch) <= 90:
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(word.upper())
else:
    print(word.lower())