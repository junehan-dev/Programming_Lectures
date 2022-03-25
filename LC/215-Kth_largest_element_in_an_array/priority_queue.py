class PriorityQueue:
    def __init__(self):
        self._datas = [None];

    def enqueue(self, x):
        self._datas.append(x);
        self._evaporate();
    
    def _evaporate(self):
        child = len(self._datas) - 1;
        parent = child // 2;
        while (parent > 0 and self._datas[parent] < self._datas[child]):
            self._swap(parent, child);
            child = parent;
            parent //= 2;

    def dequeue(self):
        ret = None;
        if len(self._datas) >= 3:
            self._swap(1, -1);
            ret = self._datas.pop();
            self._sink(1);
        elif len(self._datas) == 2:
            ret = self._datas.pop();
        return (ret);

    def _sink(self, parent):
        n = len(self._datas);
        child = None;
        r = parent*2 + 1 if n > parent*2 + 1 else None;
        l = parent*2 if n > parent*2 else None;
        if any([l, r]):
            if not r:
                child = l;
            else:
                child = r if self._datas[r] > self._datas[l] else l;
            if self._datas[child] > self._datas[parent]:
                self._swap(child, parent);
                parent = child;
                self._sink(parent);
    
    def find_max(self):
        return self._datas[1] if len(self._datas) > 1 else None;

    def _swap(self, i1, i2):
        temp = self._datas[i1];
        self._datas[i1] = self._datas[i2];
        self._datas[i2] = temp;

    def __getitem__(self, i):
        return None;

    def __setitem__(self, idx, val):
        pass;

