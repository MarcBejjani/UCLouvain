def reachable(adj_list, start_node):
    """
    Get the reachable nodes from an adjacency list using DFS.
    """
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(adj_list[node])

    return visited
