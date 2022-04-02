def dfs_recursive(node, visited):
    visited.append(node); # 메서드
    print(graph_data[node]);
    for link in graph_data[node]:
       if link not in visited:
            dfs_recursive(link, visited);

    return visited;
