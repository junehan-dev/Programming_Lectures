import heapq


def solution(n, times):
    immig_q = list((map(lambda el: [el, el], times)))
    heapq.heapify(immig_q);
    ret = 0;
    while n > 0:
        solve_cnt, spent = solve_one(immig_q);
        ret += spent;
        n -= solve_cnt;

    """
    while n > 0:
        spent, solve = cycle(times);
        ret += spent
        n -= solve;
    """
    return (ret);

def solve_one(immig_q):
    least_time = immig_q[0][0];
    print("least_time", least_time);
    coops = [_ for _ in filter(lambda el: el[0] == least_time, immig_q)];
    print("coops", coops);
    for _ in coops:
        heapq.heappop(immig_q);
    list(map(lambda el: spend_time(el, least_time), immig_q));
    solve_cnt = len(coops)
    list(map(restore_time,coops));
    print("restored", coops);
    for v in coops:
        heapq.heappush(immig_q, v)
    print(immig_q);
    return (solve_cnt, least_time)

def restore_time(el):
    el[0] = el[1];

def spend_time(immig, time):
    immig[0] -= time;

n = 6;times = [7, 10];expect=28;
assert(solution(n,times) == expect);

