class TreeNode(object):
    def __init__(self, v):
        self._v = v
        self.left = None
        self.right = None

    @property
    def value(self):
        return self._v;
        
    @value.setter
    def value(self, v):
        self._v = v;

    #For graphic
    @property
    def val(self):
        return self._v;

    @staticmethod
    def dfs_traverse(root, i,cb = print):
        if root.left:
            TreeNode.dfs_traverse(root.left, i*2 + 1);
        if root.right:
            TreeNode.dfs_traverse(root.right, i*2 + 2);
        cb(f"{i}:   value:{root}" );
        return self;

    def __str__(self):
        return f"{self._v}";

