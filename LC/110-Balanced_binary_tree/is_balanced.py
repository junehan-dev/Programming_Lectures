from tree_node import TreeNode

def is_balanced(t):
    log = [0];
    dfs_height(t, log);

    if log[0]:
        return False;
    return True;

def dfs_height(root: TreeNode, log) -> bool:
    if not root.left and not root.right:
        return (0);

    l_h = (1 + dfs_height(root.left)) if root.left else 0;
    r_h = (1 + dfs_height(root.right)) if root.right else 0;

    if abs(l_h - r_h) > 1:
        log[0] += 1;
    return max((l_h, r_h));

