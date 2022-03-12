class Node:
    def __init__(self, v = None, n = None):
        self._v = v;
        self._n = n if isinstance(n, self.__class__) else None;
    @property
    def next(self):
        return (self._n);

    @next.setter
    def next(self, v):
        self._n = v;

    @property
    def val(self):
        return (self._v);

    @val.setter
    def val(self, v):
        self._v = v;

    def __str__(self):
        return (f"{self.val}");

    def __iter__(self):
        while self.next:
            return self.next;

    @staticmethod
    def make_sequence(vals):
        *f, tail = list(map(Node, vals));
        while f:
            f[-1].next = tail;
            *f, tail = f;
        return (tail);

