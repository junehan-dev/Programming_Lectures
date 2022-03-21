def dfs(n, row = 0, log=[]):
    if not log:
        log = [-1] * n;
    ret = [];
    if row == n:
        return [[_ for _ in log]];
    for col in range(n):
        if is_valid(log, row, col):
            log[row] = col;
            ret += (dfs(n, row+1, log));
        else:
            continue;
    return ret;

def is_valid(log, row, col):
    p_row = 0;
    for old_row in range(row):
        old_col = log[old_row];
        if old_col == col:
            return False;
        diff = (col - old_col); 
        diff = ~diff + 1 if diff < 0 else diff;
        if diff == row - old_row:
            return False;
    return True;

ret = dfs(11);

print(f"max : {len(ret)}", ret);
