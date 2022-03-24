from collections import deque

def count_island(g):
    start = (0, 0);
    row_siz = len(g[0]);
    col_siz = len(g);
    counter = 0;
    rel_q = deque();
    for col in range(col_siz):
        for row in range(row_siz):
            if g[col][row] == "1":
                counter += 1;
                rel_q.append([(col, row)]);
                bfs(g, rel_q)
    return (counter);

def bfs(g, rel_q):
    rels = rel_q.popleft();
    while rels:
        lower_rels = []; # list up level
        for node in rels:
            set_zero(g, node); # set level nodes to 0
            children = parse_link(g,node); 
            lower_rels += children;
        rel_q.append(list(set(lower_rels)));
        rels = rel_q.popleft();

def set_zero(g,node):
    m, n = node;
    g[m][n] = '0';

def parse_link(g,vertex):
    m, n = vertex
    colcnt = len(g);
    rowcnt = len(g[0]);
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
            if g[xm][xn] == '1':
                ret.append((xm, xn));
    return (ret);
