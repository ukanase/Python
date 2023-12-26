from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:       
       
        def buildGraph():
            for edge in edges:
                src = edge[0]
                dest = edge[1]
                adjList[src].append(dest)
                adjList[dest].append(src)        
        
        def bfs(source):
            visited[source]
            queue = deque([source])

            while queue:
                node = queue.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:                        
                        # discovered
                        visited[neighbor] = 1                        
                        queue.append(neighbor)

        # build graph 
        adjList = [[] for _ in range(n)]
        buildGraph()
        
        # traverse using bfs or dfs
        components = 0
        visited = [-1] * n        
        
        for i in range(n):
            if visited[i] == -1:
                components += 1
                bfs(i)

        return components

s = Solution()
r = s.countComponents(4, [[0, 1],[1, 2],[0, 2]])
print(r)

