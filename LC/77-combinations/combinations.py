from collections import Counter
def combination(n, k):
    ret = []
    src = list(range(1, n+1));
    sets = permutation([], src, k);
    [ret.append(c)for c in iter(map(Counter, sets)) if c not in ret]
    return [list(uniq.keys())for uniq in ret];

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
