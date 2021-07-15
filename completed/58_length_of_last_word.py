class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])
        

s = "a "
print(Solution().lengthOfLastWord(s))