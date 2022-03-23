def permutation(dest, src):
    ret = [];
    if not src:
        return ([dest]);
    for base in src:
        nsrc = [ch for ch in src if ch is not base];
        permutations = permutation(dest + [base], nsrc);
        ret += (permutations);
    return (ret);

if __name__ == "__main__":
    nums = [1,2,3,4];
    ret = permutation([], nums);
    print(ret);
