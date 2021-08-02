class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary string을 int형 배열로 변경 후 합을 구한다.
        return sum([int(i) for i in bin(n)[2:]])


if __name__ == '__main__':
    assert 3 == Solution().hammingWeight(11)
    assert 3 == Solution().hammingWeight(7)
