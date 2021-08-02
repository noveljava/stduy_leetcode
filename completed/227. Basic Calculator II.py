class Solution:
    def operator(self, l_number, r_number, operator):
        result = 0
        if operator == "*":
            result = l_number * r_number
        elif operator == "/":
            result = l_number // r_number
        elif operator == "+":
            result = l_number + r_number
        elif operator == "-":
            result = l_number - r_number

        return result

    def calculate(self, s: str) -> int:
        operator_lower = ["+", "-"]
        operator_high = ["*", "/"]
        operator_list = operator_high + operator_lower

        number_stack = []
        operator_stack = []

        number = 0
        operator = ""

        for e in s:
            if e.isnumeric():
                number *= 10
                number += int(e)

            elif e in operator_list:
                if len(operator_stack) == 0:
                    operator_stack.append(e)
                    number_stack.append(number)
                    number = 0
                else:
                    if e in operator_lower:
                        # +, -가 들어왔을 경우에는, 앞에 있던 계산을 다 처리 해줘야한다.
                        while len(operator_stack) != 0:
                            number = self.operator(number_stack.pop(), number, operator_stack.pop())

                    # *, -일 경우에는, 바로 직전에 같은 레벨일 경우에 처리를 해줘야한다.
                    elif e in operator_high and operator_stack[-1] in operator_high:
                        number = self.operator(number_stack.pop(), number, operator_stack.pop())

                    number_stack.append(number)
                    number = 0
                    operator_stack.append(e)

        while len(operator_stack) != 0:
            number = self.operator(number_stack.pop(), number, operator_stack.pop())

        return number


if __name__ == '__main__':
    assert 7 == Solution().calculate("3+2*2")
    assert 1 == Solution().calculate(" 3/2 ")
    assert 5 == Solution().calculate(" 3+5 / 2 ")
    assert 14 == Solution().calculate(" 13+2 / 2 ")
    assert 5 == Solution().calculate("2 + 3 + 2 / 5 * 10")
    assert 1 == Solution().calculate("1-1+1")
    assert 10 == Solution().calculate("2*2+6")
    assert -24 == Solution().calculate("1*2-3/4+5*6-7*8+9/10")



    # Solution().calculate("   1234*3+2/   152")
