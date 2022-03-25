class MaxPQ:
    def __init__(self):
        self._keys = [None];

    def max(self):
        return self._keys[1] if len(self._keys) > 1 else None;

    def insert(self, x):
        self._keys.append(x);
        self._evaporate();

    def delMax(self):
        self._swap(1, -1);
        ret = self._keys.pop();
        self._sink(1);
        return (ret);

    def isEmpty(self):
        return (True if len(self._keys) == 1 else False);

    def size(self):
        return (len(self._keys) - 1);
   
    def _evaporate(self):
        child = len(self._keys) - 1;
        parent = child // 2;
        while (parent > 0 and self._keys[parent] < self._keys[child]):
            self._swap(parent, child);
            child = parent;
            parent //= 2;

    def _sink(self, parent):
        l = parent * 2 if len(self._keys) - 1 >= parent * 2 else None; 
        r = parent * 2 + 1 if len(self._keys) - 1 >= parent * 2 + 1 else None;
        if any([l, r]):
            child = r if r is not None and self._keys[r] >= self._keys[l] else l;
            if self._keys[child] > self._keys[parent]:
                self._swap(parent, child);
                self._sink(child);

    def _swap(self, i1, i2):
        temp = self._keys[i1];
        self._keys[i1] = self._keys[i2];
        self._keys[i2] = temp;

