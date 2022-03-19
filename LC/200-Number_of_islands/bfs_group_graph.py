from pprint import pprint
from collections import deque
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
    start = (0, 0);
    row_siz = len(grid[0]);
    col_siz = len(grid);
    counter = 0;
    rel_q = deque();
    for col in range(col_siz):
        for row in range(row_siz):
            if grid[col][row] == "1":
                counter += 1;
                rel_q.append([(col, row)]);
                bfs(g, rel_q)
    return (counter);

def bfs(g, rel_q):
    rels = rel_q.popleft();
    while rels:
        lower_rels = []; # list up level
        for node in rels:
            set_zero(node); # set level nodes to 0
            children = parse_link(node); 
            lower_rels += children;
            print(node, ": chilren:", children);
        pprint(g);
        print("sum of chilren:", lower_rels);
        rel_q.append(list(set(lower_rels)));
        rels = rel_q.popleft();

def set_zero(node):
    m, n = node;
    grid[m][n] = '0';

def parse_link(vertex):
    m, n = vertex
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
ret = count_island(grid);

