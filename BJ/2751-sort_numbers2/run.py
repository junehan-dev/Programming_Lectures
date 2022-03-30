from heapq import heappop, heappush

ret = [];
lines = int(input());
[heappush(ret, int(input())) for _ in range(lines)]
[print(heappop(ret)) for _ in range(lines)]


