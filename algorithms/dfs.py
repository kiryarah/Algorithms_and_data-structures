def dfs_dp(start, graph):
    visited = set()
    queue = [start]

    while queue:
        current_vertex = queue.pop()
        visited.add(current_vertex)

        for vertex in graph[current_vertex]:
            if vertex not in visited:
                queue.append(vertex)
    return visited


def dfs_recursive(start, graph, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for vertex in graph[start] - visited:
        dfs_recursive(vertex, graph, visited)
    return visited
