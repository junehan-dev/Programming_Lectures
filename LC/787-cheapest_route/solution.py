from typing import List
from collections import deque

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    log = [-1] * (n);
    log[src] = 0;
    log_g = 10000;
    q = deque(get_dest(flights, src, k, 0, log))
#    print(q);
    while q:
        out = q.popleft();
        src, k, price, log = out
        if src != dst and k > -1 and log[src] == -1:
            makelog(log, src, price);
            [q.append(_) for _ in get_dest(flights, src, k, price, log)];
        elif k >= -1 and src == dst and log_g > price:
            log_g = price;
            makelog(log, src, price);
            print(log);
        else:
            pass
    return log_g;

def makelog(log, src, price):
    log[src] = price;

def is_valid(src, price, log):
    return (True if (log[src] >= price or log[src] == -1) else False);

def get_dest(flights, src, k, price, log):
    dests = [_ for _ in (filter(lambda flight: flight[0] == src, flights))]
    if not dests:
        return [];
    [_ for _ in map(lambda flight: set_dest(flight, k-1, price, log), dests)];
    return (dests);

def set_dest(flight,k, price, log):
    flight[0] = flight[1];
    flight[1] = k;
    flight[2] = flight[2] + price;
    if len(flight) == 3:
        flight.append(log + []);
    else:
        flight[3] = log + [];


"""
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
"""

n = 18
flights = [[16,1,81],[15,13,47],[1,0,24],[5,10,21],[7,1,72],[0,4,88],[16,4,39],[9,3,25],[10,11,28],[13,8,93],[10,3,62],[14,0,38],[3,10,58],[3,12,46],[3,8,2],[10,16,27],[6,9,90],[14,8,6],[0,13,31],[6,4,65],[14,17,29],[13,17,64],[12,5,26],[12,1,9],[12,15,79],[16,11,79],[16,15,17],[4,0,21],[15,10,75],[3,17,23],[8,5,55],[9,4,19],[0,10,83],[3,7,17],[0,12,31],[11,5,34],[17,14,98],[11,14,85],[16,7,48],[12,6,86],[5,17,72],[4,12,5],[12,10,23],[3,2,31],[12,7,5],[6,13,30],[6,7,88],[2,17,88],[6,8,98],[0,7,69],[10,15,13],[16,14,24],[1,17,24],[13,9,82],[13,6,67],[15,11,72],[12,0,83],[1,4,37],[12,9,36],[9,17,81],[9,15,62],[8,15,71],[10,12,25],[7,6,23],[16,5,76],[7,17,4],[3,11,82],[2,11,71],[8,4,11],[14,10,51],[8,10,51],[4,1,57],[6,16,68],[3,9,100],[1,14,26],[10,7,14],[8,17,24],[1,11,10],[2,9,85],[9,6,49],[11,4,95]]
src = 7;
dst = 2;
k = 6;

ret = findCheapestPrice(n, flights, src, dst, k);

print(ret);
assert(ret == 169);

