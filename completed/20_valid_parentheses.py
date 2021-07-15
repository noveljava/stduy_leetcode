class Solution:
    def isValid(self, s: str) -> bool:
        open_str = ['(', '{', '[']
        match_info = dict()
        match_info[')'] = open_str[0]
        match_info['}'] = open_str[1]
        match_info[']'] = open_str[2]

        stack: list = []
        for e in s:
            if e in open_str:
                stack.append(e)
            elif len(stack) == 0 or match_info[e] != stack.pop():
                return False

        if len(stack) != 0:
            return False

        return True
