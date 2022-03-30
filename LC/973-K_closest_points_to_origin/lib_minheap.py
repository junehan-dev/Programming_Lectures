def build(srcs):
    ret = [];
    [swim(ret, src) for src in srcs]

    return (ret);

def swim(dest, src, cmp_func = (lambda a, b: a - b)):
    dest.append(src);
    i = len(dest);
    while i // 2 != 0 and cmp_func(dest[i // 2 - 1], dest[i - 1]) > 0:
        _swap(dest, i - 1, i//2 - 1);
        i //= 2;

    return (i - 1);

def _swap(src, s1, s2):
    src[s1], src[s2] = src[s2], src[s1];


