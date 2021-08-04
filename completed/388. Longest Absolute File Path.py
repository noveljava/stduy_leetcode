from typing import List

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        file_structure = input.split("\n")
        # 초기 상태. 깊이는 -1 이고, 길이는 0
        stack = [(-1, 0)]

        max_len = 0
        for file in file_structure:
            depth = file.count("\t")
            file = file[depth:]

            # 현재 깊이가, 바로 직전의 깊이보다 적다면, 앞에서의 depth는 다 순회한 것이므로 없애준다.
            while stack and depth <= stack[-1][0]:
                stack.pop()

            if "." not in file:
                # 폴더를 순회하면서 길이를 계산해준다
                stack.append((depth, len(file) + stack[-1][1] + 1))
            else:
                max_len = max(max_len, len(file) + stack[-1][1])

        return max_len

if __name__ == '__main__':
    assert 20 == Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    assert 32 == Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    assert 12 == Solution().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")
    assert 0 == Solution().lengthLongestPath("a")
