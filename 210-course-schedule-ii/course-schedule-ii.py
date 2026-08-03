from collections import deque

class Solution:

    def findOrder(self, numCourses, prerequisites):

        graph = {}

        indegree = [0] * numCourses

        # Create graph
        for i in range(numCourses):
            graph[i] = []

        # Add edges
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        # Add nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:

            node = queue.popleft()

            order.append(node)

            for nei in graph[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(order) == numCourses:
            return order

        return []