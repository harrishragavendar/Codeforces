string = input()
ones = string.count("1")
twos = string.count("2")
threes = string.count("3")
res = []
for _ in range(ones):
    res.append("1+")
for _ in range(twos):
    res.append("2+")
for _ in range(threes):
    res.append("3+")
print(''.join(res)[:-1])