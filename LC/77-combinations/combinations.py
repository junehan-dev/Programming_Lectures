from collections import Counter
def combination(n, k):
    ret = []
    src = list(range(1, n+1));
    sets = permutation_2([], src, k);
    #iters = [ret.append c for c in iter(map(Counter, sets)) if c not in ret)]
    return (sets);

def permutation_2(dest, src, k):
    if k and not src:
        return ([]);
    if not k:
        return ([dest]);
    ret = [];
    for base in src:
        nsrc = src[src.index(base) + 1:];
        permutations = permutation_2(dest + [base], nsrc, k-1);
        ret += (permutations);
    return (ret)
        

def permutation(dest, src, k):
    if not k:
        return ([dest]);
    ret = [];
    for base in src:
        nsrc = [ch for ch in src if ch is not base];
        permutations = permutation(dest + [base], nsrc, k-1);
        ret += (permutations)
    return (ret);

if __name__ == "__main__":
    ret = combination(4, 2)
    print(ret);
