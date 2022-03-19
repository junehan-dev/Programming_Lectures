def subsets_dfs(dest, src, k):
    if not k:
        return [dest];
    ret = [];
    if not src:
        return [];
    for base in src:
        """
        nsrc = [ch for ch in src if ch is not base];
        perms = subsets_dfs(dest + [base], nsrc)
        ret += perms ;
        """
        combsrc = src[src.index(base) + 1:];
        combs = subsets_dfs(dest + [base], combsrc, k-1)
        ret += combs;
    return (ret);

if __name__ == "__main__":
    ret =  subsets_dfs([], [0], 1);
    print(ret);
