def dfs(choices, n, log = 0):
    counter = 0;
    if log is n:
        return 1;
    elif log > n:
        return 0;
    else:
        for v in choices:
            if log + v <= n:
                counter += dfs(choices, n, log + v);
    return counter;

def run():
    cnt = int(input());
    while cnt:
        goal = int(input());
        ret = dfs([1,2,3],goal);
        print(ret);
        cnt -= 1;

run();
