from heapq import heappush,heappop
from functools import reduce

tmp = [];
lines = int(input());
[heappush(tmp, int(input())) for _ in range(lines)];
ret = 0;

while len(tmp) != 1:
    out = (heappop(tmp) + heappop(tmp))
    ret += out;
    heappush(tmp, out);

print(ret);

