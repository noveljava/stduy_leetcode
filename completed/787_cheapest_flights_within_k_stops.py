from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        Q = [(0, K+1, src)]

        while Q:
            time, K, node = heapq.heappop(Q)

            if node == dst:
                return time

            if K > 0:
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, K-1, v))

        return -1


# n = 5
# edges = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
# src = 0
# dst = 4
# k = 1

# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1

n = 3
edges = [[0,1,2],[1,2,1],[2,0,10]]
src = 1
dst = 2
k = 1

print(Solution().findCheapestPrice(n, edges, src, dst, k))
