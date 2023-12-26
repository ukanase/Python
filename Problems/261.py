from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def buildGraph():
            for edge in edges:
                src = edge[0]
                dest = edge[1]
                adjList[src].append(dest)
                adjList[dest].append(src)        
        
        def dfs(node, parent = -1):
            visited[node] = 1
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:                    
                    dfs(neighbor, node)
                # cycle condition if neighbor not a parent and visited node                 
                elif neighbor != parent :
                    return True
            
            return False

        # build graph 
        adjList = [[] for _ in range(n)]
        buildGraph()
        
        # traverse using bfs or dfs
        components = 0
        visited = [-1] * n        
        parents = [-1] * n
        
        for i in range(n):
            if visited[i] == -1:
                components += 1
                if dfs(i) == True: # cycle condition
                    return False
        # for graph to be valid tree, all nodes should be connected i.e. graph should be 1 connected component
        return components == 1

        