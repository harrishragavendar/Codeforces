n = int(input())
database = {}
for _ in range(n):
    name = input()
    if name in database:
        cnt = database[name] + 1
        database[name] += 1
        print(f"{name}{cnt}")
    else:
        database[name] = 0
        print("OK")