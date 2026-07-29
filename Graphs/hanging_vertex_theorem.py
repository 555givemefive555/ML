from collections import deque

def search_leaf_node(graph):
        for string in graph:
            if sum(string) == 1:
                return True
        return False

    def bfs_exist(graph, start, all_vertexes):

        queue = deque([start])
        visited = {start}

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        for elem in all_vertexes:
            if elem not in visited:
                return False
        return True


    N = int(input())
    vertexes = list(input().split())
    M = int(input())
    graph_matrix = [[0 for i in range(N)] for i in range(N)]
    for i in range(M):
        start, end = input().split()
        start_digit = vertexes.index(start)
        end_digit = vertexes.index(end)
        graph_matrix[start_digit][end_digit] = 1
        graph_matrix[end_digit][start_digit] = 1
    
    graph = dict()
    for i in range(N):
        neighbors = []
        for j in range(N):
            if graph_matrix[i][j] == 1:
                neighbors.append(vertexes[j])
            graph[vertexes[i]] = neighbors
    start_graph = list(graph.keys())[0]
    if bfs_exist(graph, start_graph, vertexes) and search_leaf_node(graph_matrix):
        print("YES")
    else:
        print("NO")
