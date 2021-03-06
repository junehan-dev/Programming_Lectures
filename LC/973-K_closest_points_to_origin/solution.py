from typing import List
from doctest import testmod
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        >>> Solution().kClosest([[1,3],[-2,2]], 1);
        [[-2,2]];
        >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2);
        [[3,3],[-2,4]]
        >>> Solution().kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3);
        []
        >>> Solution().kClosest([[-4, -7],[-4, -8],[-2,10],[10,7]], 3);
        [[-4, -7],[-4,-8], [-2,10]]
        """
        min_q = build(points);
        return [del_min(min_q) for i in range(k)];

def is_far(a, b):
    a = sqrt(a[0] ** 2 + a[1] ** 2);
    b = sqrt(b[0] ** 2 + b[1] ** 2);
    if (a > b):
        return (1);
    return (0);

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
    if dest:
        swap(dest, 0, -1);
        ret = dest.pop();
        i = 0;
        size = len(dest);
        while (not is_valid(dest, size, i)):
            l = i * 2 + 1;
            r = l + 1;
            if size < r + 1:
                swap_i = l;
            else:
                swap_i = l if is_far(dest[l], dest[r]) <= 0 else r;
            swap(dest, swap_i, i);
            i = swap_i;
        return (ret);
        
def is_valid(src, size, i):
    l = i * 2 + 1;
    r = l + 1;
    if (size < l + 1):
        return True;
    if size == l + 1:
        return (is_far(src[i], src[l]) <= 0);
    return True if is_far(src[i], src[l]) <= 0 and is_far(src[i], src[r]) <= 0 else False;

def swap(src, s1, s2):
    src[s1], src[s2] = src[s2], src[s1];

testmod();
