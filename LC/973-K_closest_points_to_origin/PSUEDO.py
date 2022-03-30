inputs = [[1,3], [-2,2]]
k = 1;

def solution():
    minheap = BinaryMinheap(inputs);

    ret = [];
    while (k != 0):
        ret.append(minheap.delete_max());
        k -= 1;

    return (ret);

def build_minheap(arr):
    for v in arr:
        pass

def calc_distance(x, y):
    return sqrt(x**2 + y**2);

