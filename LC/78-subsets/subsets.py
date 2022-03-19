def subsets_dfs(dest, src):
    if not src:
        return [dest];
    ret = [];
    for base in src:
        nsrc = [ch for ch in src if ch is not base];
        combs = subsets_dfs(dest + [base], nsrc)
        ret += combs;
    return (ret);

if __name__ == "__main__":
    ret =  subsets_dfs([], [1,2,3]);
    print(ret);
