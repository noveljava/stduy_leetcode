class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        value = [1 for _ in range(n)]
        value[0] = 0
        value[1] = 0

        for x in range(2, n):
            for i in range(x, n):
                if x*i >= n:
                    break

                value[x*i] = 0

        return sum(value)


if __name__ == '__main__':
    assert 4 == Solution().countPrimes(10)
    assert 0 == Solution().countPrimes(0)
    assert 0 == Solution().countPrimes(2)
    assert 1 == Solution().countPrimes(3)
