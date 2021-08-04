class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif j == 0:
                    # 현재 문자가 s3랑 일치하고, 바로 전 문자까지 True 였다면 True
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                elif i == 0:
                    # 현재 문자가 s3랑 일치하고, 바로 전 문자까지 True 였다면 True
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                else:
                    # 현재 조합에서 가능한지 판단 여부는, 행렬의 위와 옆을 살펴봐야한다.
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]

    def isInterleave_time_out(self, s1: str, s2: str, s3: str) -> bool:
        def recv(s1: str, s2: str, s3: str) -> bool:
            for i, x in enumerate(s3):
                if len(s1) and len(s2):
                    if s1[0] == x and s2[0] == x:
                        try_1 = recv(s1[1:], s2, s3[i + 1:])
                        try_2 = True
                        if not try_1:
                            try_2 = recv(s1, s2[1:], s3[i + 1:])
                        else:
                            return True

                        if not try_2:
                            return False
                        else:
                            return True

                    elif s1[0] == x:
                        s1 = s1[1:]
                    elif s2[0] == x:
                        s2 = s2[1:]
                    else:
                        return False

                elif len(s1) == 0 and len(s2) and s2[0] == x:
                    s2 = s2[1:]
                elif len(s1) and len(s2) == 0 and s1[0] == x:
                    s1 = s1[1:]
                else:
                    return False

            return len(s1) == 0 and len(s2) == 0

        return recv(s1, s2, s3)


if __name__ == "__main__":
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
    # assert not Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
    # assert Solution().isInterleave("", "", "")
    # assert not Solution().isInterleave("a", "b", "a")
    # assert not Solution().isInterleave("a", "b", "b")
    # assert not Solution().isInterleave(
    #     "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
    #     "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
    #     "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab",
    # )
