from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 길찾기 문제처럼, 자신의 선택지에서 가장 작은 숫자를 선택하여 결과물을 도출해낸다.
        # 그리고, 마지막까지 다 돌고 나면 마지막 줄에서 가장 작은 숫자를 선택한다.

        for row, row_array in enumerate(triangle):
            for i, v in enumerate(row_array):
                if row != 0:
                    if i == 0:
                        row_array[i] += triangle[row-1][i]
                    elif i == (len(row_array)-1):
                        row_array[i] += triangle[row-1][i-1]
                    else:
                        row_array[i] += min(triangle[row-1][i-1], triangle[row-1][i])

        return min(triangle[-1])


if __name__ == '__main__':
    assert 5 == Solution().minimumTotal([[2], [3, 10]])
    assert 11 == Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 13]])
    assert -10 == Solution().minimumTotal([[-10]])
