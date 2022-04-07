import heapq

def solution(n, times):
    immig_q = list((map(lambda el: [el, el], times)))
    ret = 0;
    heapq.heapify(immig_q);
    while n > 0:
        solve_cnt, spent = solve_one(immig_q);
        ret += spent;
        n -= solve_cnt;

    return (ret);

def solve_one(immig_q):
    coops = [heapq.heappop(immig_q)];
    least_time = coops[0][0];
    while coops[-1][0] == least_time:
        coops[-1][0] = coops[-1][1];
        coops.append(heapq.heappop(immig_q));
    heapq.heappush(immig_q, coops.pop());
    for i, _ in enumerate(immig_q):
        immig_q[i][0] -= least_time;
    for el in coops:
        heapq.heappush(immig_q, el);
    return (len(coops), least_time)

n = 6;times = [7, 10];expect=28;
assert(solution(n,times) == expect);

