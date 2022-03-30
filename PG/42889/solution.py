from three_p_qsort import three_p_qsort

def calc_ratio(stages, n):
    entered = 0;
    cur = 0;
    ret = {};
    if stages[entered] == n + 1:
        while (entered < len(stages) and stages[entered] == n+1):
            entered+=1;
    while n:
        while entered + cur < len(stages) and stages[entered+cur] == n:
            cur += 1;
        entered += cur;
        if cur:
            if f"{cur/entered}" in ret:
                ret[f"{cur/entered}"].append(n);
            else:
                ret.update({f"{cur/entered}":[n]});
        else:
            if "0" in ret:
                ret["0"].append(n);
            else:
                ret.update({"0":[n]});

        n -= 1;
        cur = 0;
    return (ret);
     
def run(arr, n):
    three_p_qsort(arr, 0, len(arr) - 1);
    logs = calc_ratio(arr, n);
    keys = sorted(logs.keys(), reverse=True);
    ret = [];
    print(logs);
    for k in keys:
        i = logs[k];
        if len(i) > 1:
            i.sort();
        ret += i;
    return (ret);

assert(run([2,1,2,6,2,4,3,3], 5) == [3,4,2,1,5]);
assert(run([4,4,4,4,4], 4) == [4,1,2,3]);


