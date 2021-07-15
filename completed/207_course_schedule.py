from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ingreed : 진입차수.
        ingreed = {}
        visited = {}

        for i in range(numCourses):
            ingreed[i] = 0
            visited[i] = False

        for course, neccessary_course in prerequisites:
            ingreed[neccessary_course] += 1

        def topological_sort():
            queue = []
            for node, value in ingreed.items():
                if value == 0:
                    queue.append(node)
                    visited[node] = True

            while True:
                if not queue:
                    return sum(visited.values()) == numCourses

                # 간선을 제거한다.
                current_course = queue.pop()
                for course, neccessary_course in prerequisites:
                    if current_course == course and ingreed[neccessary_course] != 0:
                        ingreed[neccessary_course] -= 1
                        if ingreed[neccessary_course] == 0:
                            queue.append(neccessary_course)
                            visited[neccessary_course] = True

        return topological_sort()

# numCourses = 4
# prerequisites = [[1,0],[2,1],[1,2]]
# numCourses = 3
# prerequisites = [[0, 1], [0, 2], [1, 2]]
# prerequisites = [[0, 1], [1, 0]]

# numCourses = 3
# prerequisites = [[0, 1], [1, 2], [2, 1]]
numCourses = 2
prerequisites = [[1, 0]]
print(Solution().canFinish(numCourses, prerequisites))
