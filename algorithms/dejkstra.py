from data_structure.heap import HeapMin


def get_path(start, end, visited):

    current_node, path = end, [end]

    while current_node != start:
        try:
            current_node = visited[current_node]
            path.append(current_node)
        except KeyError:
            return f'Нет такого пути! {start} -> {end}'

    return path[::-1]


def dejkstra(start, end, graph):
    queue = HeapMin((0, start))
    visited = {start: None}
    weight_visited = {start: 0}

    while queue:
        _, current_node = queue.pop()
        if current_node == end:
            break

        next_nodes = graph[current_node]

        for weight, node in next_nodes:
            new_weight = weight_visited[current_node] + weight
            if node not in weight_visited or new_weight < weight_visited[node]:
                queue.push((new_weight, node))
                weight_visited[node] = new_weight
                visited[node] = current_node

    return get_path(start, end, visited), weight_visited[end]
