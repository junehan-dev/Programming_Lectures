from pprint import pprint
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def count_island():
    cnt: int; #ISLANDS
    cnt = 0;
    rowcnt = len(grid[0]);
    colcnt = len(grid);
    
    for m in range(colcnt):
        for n in range(rowcnt):
            if grid[m][n] == '1':
                cnt += 1;
                bubling_dfs([(m, n)]);
    return cnt;

def bubling_dfs(stack):
    if not stack:
        return 0;
    m, n = stack.pop();
    grid[m][n] = '0';

    distance = 1;
    # SET (m-1, n) (m+1, n) (m, n-1) (m, n+1);
    # 4time 
        if 1 in SET: PUSE
    while stack:
        bubling_dfs(stack);
    return del_count;


    
                
count_island();
pprint(grid);
