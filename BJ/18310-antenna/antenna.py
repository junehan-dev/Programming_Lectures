def placement(cnt, houses):
    qsort(houses, 0, cnt);
    return houses[(cnt - 1) // 2];

def qsort(arr, low, high):
    if len(arr[low:high]) > 1:
        return None;
    mid = ((low + high) // 2)
    pivot = arr[mid];
    start = low + 1;
    end = high - 1;

    arr[low], arr[mid] = arr[mid], arr[low];
    while (start < end):
        if start < end and arr[start] <= pivot:
            start += 1;
        if end > start and arr[end] > pivot:
            end -= 1;
        if arr[start] > pivot and arr[end] <= pivot:
            arr[start], arr[end] = arr[end], arr[start];

    start -= 1;
    arr[low], arr[start] = arr[start], arr[low];
    qsort(arr, low, start - 1);
    qsort(arr, start + 1, high);
