from typing import List
from collections import deque

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    q = deque(get_dest(flights, src, k, 0))
    log = [-1] * (n);
    log[src] = 0;
    while q:
        src, k, price = q.popleft();
        if src != dst and k > -1 and is_valid(src, price, log):
            makelog(log, src, price);
            [q.append(_) for _ in get_dest(flights, src, k, price)];
        elif k >= -1 and src == dst and is_valid(src, price, log):
            makelog(log, src, price);
        else:
            print(f"{k}lefts, to {src} failed. {log}");
    return log;

def makelog(log, src, price):
    log[src] = price;

def is_valid(src, price, log):
    print(src, log);
    return (True if (log[src] > price or log[src] == -1) else False);

def get_dest(flights, src, k, price):
    print(flights);
    dests = [_ for _ in (filter(lambda flight: flight[0] == src, flights))]
    if not dests:
        return [];
    [_ for _ in map(lambda flight: set_dest(flight, k-1, price), dests)];
    return (dests);

def set_dest(flight,k, price):
    flight[0] = flight[1];
    flight[1] = k;
    flight[2] = flight[2] + price;


n = 3;
flights = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500]
];
src = 0;
dst = 2;
k = 1;
ret = findCheapestPrice(n, flights, src, dst, k);
print(ret);
assert(ret[dst] == 200);

n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]; src = 0; dst = 2; k = 0;
ret = findCheapestPrice(n, flights, src, dst, k);
assert(ret[dst] == 500);
n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]; src = 0; dst = 2; k = 1;
ret = findCheapestPrice(n, flights, src, dst, k);
print(ret);
assert(ret[dst] == 200);
