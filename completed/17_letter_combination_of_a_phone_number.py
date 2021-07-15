from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result: List = []
        if digits == "":
            return result

        phone_info: dict = {}
        phone_info["2"] = 'abc'
        phone_info["3"] = 'def'
        phone_info["4"] = 'ghi'
        phone_info["5"] = 'jkl'
        phone_info["6"] = 'mno'
        phone_info["7"] = 'pqrs'
        phone_info["8"] = 'tuv'
        phone_info["9"] = 'xywz'

        def backtracking(digits, info):
            if "" == digits:
                result.append(''.join(info))
                return

            for ch in phone_info[digits[0]]:
                info.append(ch)
                backtracking(digits[1:], info)
                info.pop()

        backtracking(digits, [])
        return result

digits = ""
print(Solution().letterCombinations(digits))