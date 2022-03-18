graph_data = [
    [0,1,1,1,0,0,0], #1
    [0,0,0,0,1,0,0], #2
    [0,0,0,0,1,0,0], #3
    [0,0,0,0,0,0,0], #4
    [0,0,0,0,0,1,1], #5
    [0,0,0,0,0,0,0], #6
    [0,0,1,0,0,0,0], #7
#   [1,2,3,4,5,6,7]
];
#route_map = [[2, 3, 4], [5], [5], [], [6, 7], [], [3]]
#graph_dict = dict(zip(range(1,8), graph_data));

def dfs1(node, visited, log):
    if node in visited: #이미 방문했다면,
        print(node, " registed");
        return log.append(visited + [node]); #여기서 저장해야 처리가 된다.
    node_links = graph_data[node];
    #[0,1,1,1,0,0,0], #1
    if not any(node_links): # 이동할 경로가 없다면
        print(node, " no routes");
        return log.append(visited + [node]); #여기도.
    else:
        visited.append(node); 
        print(node, " added to: ", visited);
        print(node, " can move to: ", node_links);
        for link, v in enumerate(node_links):
            print(node, "move to->", link);
            dfs1(link, visited, log);

log = [];
visited = []
dfs1(0, visited, log);
print("visited: ", visited);
print("logs :", log);


"""    
def dfs_recursive(node, visited):
    visited.append(node); # 메서드
    print(graph_data[node]);
    for link in graph_data[node]:
       if link not in visited:
            dfs_recursive(link, visited);

    return visited;
"""
def dfs_stack(i):
    visited = []; 
    stack = [i];

    #여기서 for로 i의 루트정보를 묶어주고
    #엔트리 기준이 아니라, 엔트리가 갈 수 있는 곳들을 대상으로,
    # [1] 0번째 는 정해놨으니까 순열에서 첫번째 1을 대상에서 제외하고, 
    # 이동해야할 횟수 한번 줄어듬. top에 visited로 시작하는 것을 바꾸는 방식.
    while stack:
        top = stack.pop();
        visited.append(top); #첫 방문 정보 저장

        for idx, v in enumerate(graph_data[top]):# 마지막 기록의 가능한 루트정보 갱신
            if v and idx not in visited:
                stack.append(idx);
    return list((map(lambda el: el+ 1, visited)));

#route = get_route_set2(0);
#print(route);

#route_stack = dfs_stack(0);
#print(route_stack);

