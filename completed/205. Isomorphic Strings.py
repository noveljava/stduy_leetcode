class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False

        s_map = defaultdict(list)
        t_map = defaultdict(list)

        for i, x in enumerate(s):
            s_map[x].append(i)

        for i, x in enumerate(t):
            t_map[x].append(i)

        for v in s_map.values():
            if v not in t_map.values():
                return False

        for v in t_map.values():
            if v not in s_map.values():
                return False

        return True


if __name__ == '__main__':
    assert Solution().isIsomorphic("egg", "add")
    assert not Solution().isIsomorphic("foo", "bar")
    assert Solution().isIsomorphic("paper", "title")
