from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtracking(current_position, s, info):
            if current_position == 4:
                current_info = ".".join(info[:])
                if len(s) == 0 and current_info not in result:
                    result.append(current_info)
                return
            elif current_position != 4 and len(s) == 0:
                return

            for i in range(1, 4):
                current_num = int(s[:i])
                if 0 <= current_num <= 255 and len(s[:i]) == len(str(current_num)):
                    info.append(s[:i])
                    backtracking(current_position+1, s[i:], info)
                    info.pop()
                
        backtracking(0, s, [])
        return result


s = "101023"
print(Solution().restoreIpAddresses(s))