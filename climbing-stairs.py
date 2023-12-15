class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 2:
            dp = [0] * (n + 1)
            print(dp)
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[n]
        return n
    
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(7))
print(Solution().climbStairs(8))
print(Solution().climbStairs(99))