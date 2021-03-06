def three_p_qsort(arr, start, end):
    if start >= end:
        return ;

    lt_i = start;
    cur_i = start + 1;
    pivot = arr[start];
    gt_i = end;

    while (cur_i <= gt_i):
        if arr[cur_i] > pivot:
            swap(arr, lt_i, cur_i);
            lt_i += 1;
            cur_i += 1;
        elif arr[cur_i] < pivot:
            swap(arr, gt_i, cur_i);
            gt_i -= 1;
        else:
            cur_i += 1;
    if lt_i != start:
        three_p_qsort(arr, start, lt_i - 1);
    if gt_i != end:
        three_p_qsort(arr, gt_i + 1, end);

def swap(arr,s1, s2):
    arr[s1], arr[s2] = arr[s2], arr[s1];
