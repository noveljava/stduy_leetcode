from typing import List

class Solution:
    def make_graycode(self, bin_str):
        result_str = ""
        for i, ch in enumerate(bin_str):
            value = ch
            if i > 0:
                value = int(value) ^ int(bin_str[i-1])
            
            result_str += str(value)

        return int(result_str, 2)

    def grayCode(self, n: int) -> List[int]:
        result = []
        max_loop = 2**n
        for i in range(max_loop):
            result.append(self.make_graycode(str(bin(i))[2:]))
            
        return result

print(Solution().grayCode(5))