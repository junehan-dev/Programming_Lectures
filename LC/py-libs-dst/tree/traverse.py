from tree_node import TreeNode

def inorder_traverse(root: TreeNode):
    if root is None:
        return [];
    ret = [];
    ret += (inorder_traverse(root.left));
    ret += ([root.value]);
    ret += (inorder_traverse(root.right));
    return ret;

