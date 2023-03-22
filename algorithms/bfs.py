from collections import deque


def get_path(start, end, visited):

    current_node, path = end, [end]

    while current_node != start:
        try:
            current_node = visited[current_node]
            path.append(current_node)
        except KeyError:
            return f'Нет такого пути! {start} -> {end}'

    return path[::-1]


def bfs(start, end, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current_node = queue.popleft()
        if current_node == end:
            break

        next_nodes = graph[current_node]

        for node in next_nodes:
            if node not in visited:
                queue.append(node)
                visited[node] = current_node

    return get_path(start, end, visited)
