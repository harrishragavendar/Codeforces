string = input()
if len(string) > 2:
    charSet = set()
    for i in range(1, len(string)-1, 3):
        charSet.add(string[i])
    print(len(charSet))
else:
    print("0")