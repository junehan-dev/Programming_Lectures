from collections import deque;

def placement(cnt, houses):
    h_map = set(houses);
    mid = sum(houses) // cnt;
    q = deque([[mid]]);
    ret = [];
    while not ret:
        ts = q.popleft();
        ret = [t for t in ts if t in h_map];
        if not ret:
            lev = [];
            if mid - 1:
                lev.append(mid - 1);
            if mid + 1 < cnt:
                lev.append(mid + 1);
            ret.append(lev);
    return min(ret);
