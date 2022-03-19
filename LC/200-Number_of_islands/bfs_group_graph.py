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
    start = (0, 0);
    row_siz = len(grid[0]);
    col_siz = len(grid[0]);

    top = start;
    relatives = parse_link(start);
    # set top 0 and set rel 0 push rels to work Q

def parse_link(vertex):
    n, m = *vertex
    col_cnt = len(grid);
    row_cnt = len(grid[0]);
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

