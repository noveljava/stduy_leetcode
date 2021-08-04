class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 영어 문자에서 숫자를 뽑아내기 위한 보정치.
        number = 64
        result = 0
        for e in columnTitle:
            value = ord(e) - number
            # 자리수 보정.
            result *= 26
            result += value

        return result


if __name__ == '__main__':
    assert 1 == Solution().titleToNumber("A")
    assert 28 == Solution().titleToNumber("AB")
    assert 701 == Solution().titleToNumber("ZY")
    assert 2147483647 == Solution().titleToNumber("FXSHRXW")
