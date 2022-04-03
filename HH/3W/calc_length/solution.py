import bisect
from collections import Counter

def setup(d):
    dc = Counter(sorted(d));
    return ([_ for _ in zip(dc.keys(), dc.values())]);

def binsearch_slice(arr, target):
    slice_h = arr[-1][0] - 1; 
    slice_l = 0;
    slice_mid = (slice_h) // 2;

    start = 0;
    end = len(arr);

    while slice_l < slice_h:
        result, start_idx = calc_result(arr, slice_mid, start, end);
        if result > target:
            slice_l = slice_mid + 1;
            start = start_idx;
        elif result < target:
            slice_h = slice_mid - 1;
            end = start_idx;
        else:
            return (slice_mid);
        slice_mid = (slice_h + slice_l) // 2;
    return (slice_l);

def calc_result(arr, slice_mid, start, end):
    start = bisect.bisect_right(arr, slice_mid, start, end - start, key = lambda k: k[0]);
    ret = sum(map(lambda el: (el[0] - slice_mid) * el[1] , arr[start:]));
    return (ret, start);

if __name__ == "__main__":
    data = [19, 14, 10, 17, 17, 2, 2, 2];
    format_data = setup(data);
    req = 6;
    ret = binsearch_slice(format_data, req);

    req = sum(data);
    ret = binsearch_slice(format_data, req);

    req = sum(data) - 7;
    ret = binsearch_slice(format_data, req);

    req = sum(data) - 8;
    ret = binsearch_slice(format_data, req);


