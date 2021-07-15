class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        stone_info = defaultdict(int)

        for stone in stones:
            stone_info[stone] += 1

        jewels_count = 0
        for jewel in jewels:
            jewels_count += stone_info[jewel]

        return jewels_count
