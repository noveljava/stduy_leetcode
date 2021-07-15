class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while n != 1:
            history.append(n)
            sum_value = 0
            while n != 0:
                tmp = n % 10
                sum_value += tmp * tmp
                n = int(n/10)

            n = sum_value
            if n in history:
                return False

        return True


if __name__ == '__main__':
    assert Solution().isHappy(19)
    assert not Solution().isHappy(2)