string = input()
if 65 <= ord(string[0]) <= 90:
    print(string)
else:
    print(f"{chr(ord(string[0]) - 32)}{string[1:]}")