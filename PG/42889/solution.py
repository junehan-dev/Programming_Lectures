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
        if f"{cur/entered}" in ret:
            ret[f"{cur/entered}"].append(n);
        else:
            ret.update({f"{cur/entered}":[n]});
        n -= 1;
    return (ret);
     
def run(arr, n):
    three_p_qsort(arr, 0, len(arr) - 1);
    logs = calc_ratio(arr, n);
    keys = sorted(logs.keys(), reverse=True);
    ret = [];
    for k in keys:
        i = logs[k];
        if len(i) > 1:
            i.sort();
        ret += i;
    return (ret);

print(run([1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,2,2,1,3,2,4,4], 3));

