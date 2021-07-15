from typing import List


class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     from collections import defaultdict
    #     from queue import PriorityQueue

    #     INF = 101  # 1 <= time <= 100
    #     time_table = defaultdict(list)
    #     seen: List = [False] * (n+1)
    #     node_info: List = [INF] * (n+1)

    #     node_info[k] = 0
    #     current_node = k

    #     next_node = PriorityQueue()
    #     for info in times:
    #         from_node, to_node, time = info
    #         time_table[from_node].append([to_node, time])

    #     while not seen[current_node]:
    #         for info in time_table[current_node]:
    #             node, time = info
    #             node_info[node] = \
    #                 min(node_info[current_node]+time, node_info[node])

    #             if not seen[node]:
    #                 # 노드의 정보가 중복으로 들어갈수 있다.
    #                 next_node.put((node_info[node], node))

    #         seen[current_node] = True
    #         # 우선순위큐로, 시작점과 가장 가까운 노드를 찾는다.
    #         while next_node.qsize() != 0:
    #             current_node = next_node.get()[1]
    #             if not seen[current_node]:
    #                 break

    #     return max(node_info[1:]) if max(node_info[1:]) != INF else -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for u, v, w, in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = defaultdict(list)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())
        return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))