n = int(input())
ans = 0
ans += n // 5
n %= 5
ans += n // 4
n %= 4
ans += n // 3
n %= 3
ans += n // 2
n %= 2
ans += n
print(ans)