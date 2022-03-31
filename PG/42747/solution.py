from collections import Counter
def solution(citations):
    c = Counter(citations);
    keys = sorted(c.keys(), reverse=True)
    sums = 0;
    h_idx = 0;
    for i, k in enumerate(keys):
        sums += c[k];
        c[k] = sums;
        if sums >= k and h_idx <= k:
            h_idx = k;
        if sums < k and h_idx <= k:
            h_idx = sums;
        
    return h_idx;

#print(solution([10,8]))
print(solution([1,0,6,5,5,5,0]))
print(solution([1,0,6,5,5,5,0]) == 4);
