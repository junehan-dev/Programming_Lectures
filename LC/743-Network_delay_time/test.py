from typing import List
from collections import deque

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    signal_q, left = set_data(times, k);
    logs = [-1] * n;
    logs[k - 1] = 0;
    print(logs);
    print(signal_q);
    print(left);
    delay_map = find_shortest_delay(signal_q, left, logs, 1);
    print(delay_map);
    ret = -1 if -1 in delay_map else max(delay_map);
    print("ret:", ret);
    return (ret);

def set_data(times, k):
    ret = deque(filter(lambda sig: sig[0] == k,times));
    left = list(filter(lambda sig: k not in [sig[0], sig[1]], times));
    return (ret, left);

def find_shortest_delay(signal_q, left, logs, n):
    while len(signal_q):
        signal = signal_q.popleft();
        print(signal);
        signal_to       = signal[1];
        delay           = signal[-1];
        print(signal_to);
        if logs[signal_to - 1] == -1 or logs[signal_to - 1] > delay:
            logs[signal_to - 1] = delay;
            adjs = [_ for _ in filter(lambda sig: sig[0] == signal_to, left)];
            if adjs:
                adjs = [[signal[0], signal[1], signal[2] + delay] for signal in adjs];
                [_ for _ in map(lambda signal:signal_q.append(signal), adjs)];
            print("Q:",signal_q);
            print("log:",logs);

    

    return logs;
"""
times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2;
assert(networkDelayTime(times, n, k) == 2);

times = [[1,2,1]]; n = 2; k = 1;
assert(networkDelayTime(times, n, k) == 1);

times = [[1,2,1]]; n = 2; k = 2;
assert(networkDelayTime(times, n, k) == -1);
"""
times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]];
n = 5;
k = 3;

print(sorted(times, key=lambda el: el[0]));
assert(networkDelayTime(times, n, k) == 59);

