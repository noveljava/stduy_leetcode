class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        prev_result = 1
        result = 2

        for _ in range(2, n):
            prev_result, result = result, prev_result+result

        return result

