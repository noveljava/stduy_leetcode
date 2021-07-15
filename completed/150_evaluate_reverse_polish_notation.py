from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value_stack: List = []
        op = ["+", "-", "*", "/"]
        for i in tokens:
            if i in op:
                right_value = value_stack.pop()
                left_value = value_stack.pop()

                if i == "+":
                    left_value += right_value
                elif i == "-":
                    left_value -= right_value
                elif i == "*":
                    left_value *= right_value
                elif i == "/":
                    left_value /= right_value
                    left_value = int(left_value)

                value_stack.append(left_value)
            else:
                value_stack.append(int(i))


        return value_stack.pop()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
