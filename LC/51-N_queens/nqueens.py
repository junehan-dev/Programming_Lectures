from collections import deque

def main():
    n = 4;
    log = [-1] * n;
    result = []
            result.append(ret);

def dfs(log, row, n):
    if (row == n):
        return (log);
    ret = [];
    col = 0;
    while (col < n):
        print(row);
        log[row] = col;
        if check_log(log, row):
            ret += dfs(log, row + 1, n)
        col += 1;
    return (ret);

def check_log(log, row):
    cmp_row = 0;
    while (cmp_row < row):
        if log[cmp_row] == log[row]:
            return (0);
        if row - cmp_row == abs(log[row] - log[cmp_row]):
            return (0);
        cmp_row += 1;
    return (1);



main();
