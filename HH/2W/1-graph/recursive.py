graph_data = [
    [0,1,0,1,0,0,0], #1 #0
    [0,0,1,0,1,0,0], #2 #1
    [0,0,0,1,0,1,0], #3 #2
    [0,0,0,0,0,0,1], #4 #3
    [0,0,0,0,0,1,1], #5 #4
    [0,0,0,0,0,0,0], #6 #5
    [0,0,1,0,0,1,0], #7 #6
];# 왜 제일 긴게 나오는지 잘 모르겠다.
#route_map = [[2, 3, 4], [5], [5], [], [6, 7], [], [3]]
#graph_dict = dict(zip(range(1,8), graph_data));

def dfs1(node, visited, logs, badlog):
    if node == 0:
        print("FIRST: ", node);
        print(graph_data[node]);
    if node in visited: #이미 방문했다면,
        print(node, "FIN registed");
        badlog.append(visited + [node]); #여기서 visited를 복사하고, badlog에 append하면 
        return ;
    node_links = graph_data[node];
    #[0,1,1,1,0,0,0], #1
    if not any(node_links): # 이동할 경로가 없다면
        print(node, "FIN no routes");
        badlog.append(visited + [node]); #여기도.
        return ;
    else:
        visited.append(node); 
        print(node, " added to: ", visited);
        print(node, " can move to: ", node_links);
        for link, v in enumerate(node_links):
            if v:
                print(node, "move to->", link);
                dfs1(link, visited, log, badlog);
                if node == 0: ## 이 부분이 visited를 새로운 데이터로 갱신해주는 가장 바깥쪽 함수콜
                    print("MAIN 0 iter over:", link);
                    print("0 loop clean visited.");
                    logs.append(visited);
                    visited = [];
                    # 이부분을 갱신하지 않으면, 최초에 간 가장 긴 데이터만 기록이 되기 때문에, 나중에 방문한 곳, 즉 먼곳이 더 많이 순회할 수 있었다면, 기록되지 힘들다. 왜냐하면 이미 전에 방문한 VISITED에 로그에 해당 노드를 방문한 기록이 있을 가능성이 높아서.
 
        return ;

log = [];
visited = [];
badlog = []
dfs1(0, visited, log, badlog);

print("visited:", visited);
print(log);
