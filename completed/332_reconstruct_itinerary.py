from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import bisect
        from collections import defaultdict
        from_to_dict = defaultdict(list)

        # ticket 정보 update.
        for ticket in tickets:
            from_nation, to_nation = ticket[0], ticket[1]
            bisect.insort(from_to_dict[from_nation], to_nation)

        stack: List = ["JFK"]
        result: List = []

        while stack:
            while from_to_dict[stack[-1]]:
                stack.append(from_to_dict[stack[-1]].pop(0))

            result.append(stack.pop())

        return result[::-1]

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     from collections import defaultdict
    #     graph = defaultdict(list)
    #     for a, b in sorted(tickets, reverse=True):
    #         graph[a].append(b)

    #     print(graph)
    #     route = []
    #     def dfs(a):
    #         while graph[a]:
    #             dfs(graph[a].pop())
    #         route.append(a)

    #     dfs('JFK')
    #     return route[::-1]


# tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
tickets = [["JFK", "KUL"], ["JFK", "ZTA"], ["ZTA", "JFK"]]
print(Solution().findItinerary(tickets))

# ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
# ['AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL', 'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'HBA']

["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
['JFK','AXA','AUA','ADL','ANU','AUA','ANU','EZE','ADL','EZE','ANU','JFK','AXA','EZE','TIA','ADL','EZE','AUA','AXA','TIA','ADL']