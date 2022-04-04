from typing import List
from collections import deque

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    signal_q, left = set_data(times, k);
    logs = [-1] * n;
    print(logs);
    logs[k - 1] = 0;
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

def set_delay_acc(signal, delay):
    signal[-1] += delay;

def find_shortest_delay(signal_q, left, logs, n):
    while len(signal_q):
        signal   = signal_q.popleft();
        print(signal);
        signal_to       = signal[1];
        delay           = signal[-1];
        print(signal_to);
        if logs[signal_to - 1] == -1 or logs[signal_to - 1] > delay:
            logs[signal_to - 1] = delay;
            adjs = [set_delay_acc(sig, delay) or sig for sig in filter(lambda sig: sig[0] == signal_to, left) if sig];
            print("ajs", adjs);
            if adjs:
                signal_q.append(*adjs);
            else:
                print("NOT!");
            print(signal_q);

    

    return logs;
times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2;
networkDelayTime(times, n, k);

