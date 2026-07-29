from collections import deque

def bfs_exist(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == target:
            return path
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return -1

N = int(input())
graph = {}
for i in range(N):
    string = list(map(int, input().split()))
    neighbors = []
    for j in range(N):
        if string[j] == 1:
            neighbors.append(j)
    graph[i] = neighbors

start, target = map(int, input().split())
result = bfs_exist(graph, start, target)
if result == -1:
    print(-1)
else:
    print(len(result)-1)
