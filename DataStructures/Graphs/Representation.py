adjList = [[] for _ in range(3)]
# 0 - 1, 2
# 1 - 0, 2
# 2 - 1
adjList[0] = [1, 2]
adjList[1] = [0, 2]
adjList[2] = [1]

# adjList.append([1, 2])
# adjList.append([0, 2])
# adjList.append([1])

print(adjList)

# 1D 
dp = [0] * 10
print(dp)

# 2D
dp2D = [[] for _ in range(10)]
# dp2D = []
for i in range(10):
    # dp2D.append([0] * 5)
    dp2D[i].append(i+1)

print(dp2D)

