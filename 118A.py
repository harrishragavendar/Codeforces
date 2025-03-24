word = input()
ans = []
vowels = set(['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'])
for ch in word:
    if ch not in vowels:
        ans.append('.')
        ans.append(ch.lower())
print(''.join(ans))