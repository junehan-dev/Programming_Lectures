class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       pass     

def is_far(a, b):
    ret = ((a[0] ** 2 + a[1] ** 2) - (b[0] ** 2 + b[1] ** 2));
    if ret == 0:
        return 0;
    return (1 if ret > 0 else -1);

def build(srcs):
    ret = [];
    [insert(ret, src, is_far) for src in srcs]
    return (ret);

def insert(dest, src, cmp_func = (lambda a, b: a - b)):
    dest.append(src);
    i = len(dest);
    while i // 2 != 0 and cmp_func(dest[i // 2 - 1], dest[i - 1]) > 0:
        swap(dest, i - 1, i//2 - 1);
        i //= 2;

    return (i - 1);

def del_min(dest):
    if not dest:
        return None;
    swap(dest, 0, -1);
    ret = dest.pop();
    i = 0;
    size = len(dest);
    while (not is_valid(dest, size, i)):
        l = i * 2 + 1;
        r = l + 1;
        swap_i = l if dest[l] <= dest[r] else r;
        swap(dest, swap_i, i);
        i = swap_i;
    return (ret);
        
def is_valid(src, size, i):
    l = i * 2 + 1;
    r = l + 1;
    if (size < r + 1):
       return True;
    return True if src[i] <= src[l] and src[i] <= src[r] else False;

def swap(src, s1, s2):
    src[s1], src[s2] = src[s2], src[s1];

