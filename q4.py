class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count_beautiful(n):
            if n == 0:
                return 0  # Edge case

            digits = list(map(int, str(n)))  # Convert number to digit list
            dp_cache = {}  # Explicit memoization dictionary

            def dp(pos, sum_digits, prod_digits, tight):
                if pos == len(digits):
                    return 1 if sum_digits > 0 and prod_digits % sum_digits == 0 else 0  # Avoid division by zero

                # Memoization lookup
                key = (pos, sum_digits, prod_digits, tight)
                if key in dp_cache:
                    return dp_cache[key]

                limit = digits[pos] if tight else 9
                res = 0

                for d in range(0, limit + 1):  # Try all digits from 0 to limit
                    new_sum = sum_digits + d
                    new_prod = prod_digits * d if prod_digits != 0 else d  # Handle zero correctly
                    res += dp(pos + 1, new_sum, new_prod, tight and (d == limit))

                dp_cache[key] = res  # Store result in memoization table
                return res

            return dp(0, 0, 1, True)  # Start DP recursion

        return count_beautiful(r) - count_beautiful(l - 1)  # Compute in range [l, r]

# Example usage
sol = Solution()
print(sol.beautifulNumbers(10, 20))  # Output: 2
print(sol.beautifulNumbers(1, 1000000000))   # Output: 10
