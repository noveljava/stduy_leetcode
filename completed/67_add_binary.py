class Solution:
    def addBinary(self, a: str, b: str) -> str:
        left_value = int(a, 2)
        right_value = int(b, 2)
        result = left_value+right_value
        return "{0:b}".format(result)


a = "1010"; b = "1011"
print(Solution().addBinary(a, b))