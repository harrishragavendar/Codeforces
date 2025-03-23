n = int(input())
strings = [''] * n
for i in range(n):
    strings[i] = input()
for s in strings:
    if len(s) > 10:
        print(f"{s[0]}{len(s) - 2}{s[-1]}")
    else:
        print(s)