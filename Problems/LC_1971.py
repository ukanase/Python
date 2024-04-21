class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        Edge cases 
            - src and dest same 
            - no edges 
        TC: O(V + E)
        SC: O(V + E)

            buildGraph
            start dfs from source
                if destination is discovered true else false
        """
        """
        n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
        adjList 
            0 - [1, 2]
            1 - [0, 2]
            2 - [1, 0]
        visited = [1, 1, 1]
        dfs 0 
            dfs 1 
                dfs 2 
        """
        def buildGraph():
            for edge in edges:
                s = edge[0]
                d = edge[1]
                adjList[s].append(d)
                adjList[d].append(s)
        
        def dfs(cur):         
            visited[cur] = 1   
            if cur == destination: 
                return True

            for neighbor in adjList[cur] :
                if visited[neighbor] == -1:                    
                    if dfs(neighbor):
                        return True
            
            return False
            
        adjList = [[] for i in range(n)]
        visited = [-1] * n
        buildGraph()
        
        return dfs(source)

n = 4
edges = []
source = 0
destination = 3
s =  Solution()
r = s.validPath(n, edges, source, destination)
print(r)
        
        