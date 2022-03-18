from pprint import pprint
"""
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
"""
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def count_island(g):
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
    if not stack: #base
        return 0;
    m, n = stack.pop();
    grid[m][n] = '0';
    rels = get_rel_area(m, n);
    for rel in rels:
        nm = rel[0];
        nn = rel[1];
        grid[nm][nn] = '0';
        stack.append((nm,nn));
    pprint(grid);
    print(stack);
    pprint("");
    return bubling_dfs(stack);

def get_rel_area(m, n):
    colcnt = len(grid);
    rowcnt = len(grid[0]);
    rels = [
        (m-1, n),
        (m+1, n),
        (m, n-1),
        (m, n+1)
    ];
    ret = [];

    for rel in rels:
        xm, xn = rel;
        if (xm < colcnt and xn < rowcnt and xm >= 0 and xn >= 0):
            if grid[xm][xn] == '1':
                ret.append((xm, xn));
    print(f"{m},{n}: Related:", ret);
    return (ret);

    
                
pprint(grid);
print(count_island(grid));
pprint(grid);
