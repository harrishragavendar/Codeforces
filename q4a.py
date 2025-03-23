from collections import Counter

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        res = 0
        valid = set()
        for num in range(l, r+1):
            count = Counter(str(num))
            if count[0] > 0:
                res += 1
                continue
            elif frozenset(count) in valid:
                res += 1
            else:
                digitProd = 1
                digitSum = 0
                for k, v in count.items():
                    k = int(k)
                    digitProd *= (k ** v)
                    digitSum += (k * v)
                if digitProd % digitSum == 0:
                    res += 1
                    valid.add(frozenset(count.items()))
        return res

sol = Solution()
print(sol.beautifulNumbers(10, 20))  # Output: 2
print(sol.beautifulNumbers(1, 1000000000))   # Output: 10
