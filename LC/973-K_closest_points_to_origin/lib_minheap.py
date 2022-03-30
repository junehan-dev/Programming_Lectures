def build(srcs, cmp_func = (lambda a, b: a - b)):
    ret = [];
    [insert(ret, src, cmp_func) for src in srcs]

    return (ret);

def insert(dest, src, cmp_func = (lambda a, b: a - b)):
    dest.append(src);
    i = len(dest);
    while i // 2 != 0 and cmp_func(dest[i // 2 - 1], dest[i - 1]) > 0:
        swap(dest, i - 1, i//2 - 1);
        i //= 2;

    return (i - 1);

def del_min(dest, cmp_func = lambda a, b: a - b):
    if not dest:
        return None;
    swap(dest, 0, -1);
    ret = dest.pop();
    i = 0;
    size = len(dest);
    while (not is_subtree_valid(dest, size, i, cmp_func)):
        l = i * 2 + 1;
        r = l + 1;
        if size < r + 1:
            swap_i = l
        else:
            swap_i = l if dest[l] <= dest[r] else r;
        swap(dest, swap_i, i);
        i = swap_i;
    return (ret);
        
def is_subtree_valid(src, size, i, cmp_func):
    l = i * 2 + 1;
    r = l + 1;
    if (size < l + 1):
       return True;
    if (size == l + 1):
        return cmp_func(src[i], src[l]) <= 0;
    return True if cmp_func(src[i] <= src[l]) and cmp_func(src[i] <= src[r]) else False;

def swap(src, s1, s2):
    src[s1], src[s2] = src[s2], src[s1];

