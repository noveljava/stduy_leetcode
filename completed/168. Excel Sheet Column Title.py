class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        CHAR_INDEX = 64

        result = ""
        while columnNumber > 0:
            columnNumber, current_idx = divmod(columnNumber, 26)
            if current_idx == 0:
                current_idx = 26
                columnNumber -= 1

            result = chr(current_idx + CHAR_INDEX) + result

        return result


if __name__ == '__main__':
    assert Solution().convertToTitle(1) == 'A'
    assert Solution().convertToTitle(28) == 'AB'
    assert Solution().convertToTitle(701) == 'ZY'
    assert Solution().convertToTitle(2147483647) == 'FXSHRXW'
    assert Solution().convertToTitle(52) == 'AZ'
