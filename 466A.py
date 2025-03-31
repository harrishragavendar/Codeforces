import math
n, m, a, b = list(map(int, input().split()))
normal_cost = n * a
m_cost = int(math.ceil(n / m) * b)
print(min(normal_cost, m_cost))