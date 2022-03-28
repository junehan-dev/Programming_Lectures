def dfs(src, length, log=""):
    if len(log) == length:
        return ([log]);
    if not src:
        return [];

    ret = [];

    for v in src:
        idx = src.index(v);
        if len(src) - idx == 0:
            return "";
        comb = dfs(src[idx + 1:], length, f"{log}{v}");
        if comb:
            ret += comb;
    return (ret);

def run():
    #length = 3;
    #chars = sorted(['a', 't', 'c', 'i', 's', 'w']);
    length = input();
    length, chars = length.split(" ");
    length = (int(length));
    chars = input().split(" ");
    [print(comb) for comb in dfs(sorted(chars), length)];
run();
