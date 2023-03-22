def get_next_vertex(vertex, adjacency_matrix, queue):
    for i, weight in enumerate(adjacency_matrix[vertex]):
        if weight != 0 and i not in queue:
            yield i, weight


def get_current_min(total, queue):
    min_ = float('inf')
    i_min = -1

    for i, weight in enumerate(total):
        if i not in queue and min_ > weight and weight > 0:
            min_ = weight
            i_min = i
    return i_min


def route_search(n, adjacency_matrix, start, end):
    vertex = start - 1
    queue = {vertex}
    total = [float('inf')] * n
    total[vertex] = 0

    while vertex != end - 1:
        for i, weight in get_next_vertex(vertex, adjacency_matrix, queue):
            total[i] = min(total[i], total[vertex] + weight)

        vertex = get_current_min(total, queue)
        queue.add(vertex)

    return total[end - 1]
