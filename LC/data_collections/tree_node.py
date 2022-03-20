class TreeNode(object):
    def __init__(self, v):
        self._v = v
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left;

    @left.setter
    def left(self, v):
        self._left = TreeNode(v);

    @property
    def right(self):
        return self._right;

    @right.setter
    def right(self, v):
        self._right = TreeNode(v);
