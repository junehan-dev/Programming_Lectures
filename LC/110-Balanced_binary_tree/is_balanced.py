def is_balanced(root):
    if root is None:
        return True;
    log = [0];
    dfs_height(root, log);
    return False if log[0] True else False;

def dfs_height(root: TreeNode, log) -> bool:
    l_h = (1 + dfs_height(root.left)) if root.left else 0;
    r_h = (1 + dfs_height(root.right)) if root.right else 0;

    if abs(l_h - r_h) > 1:
        log[0] += 1;
    return max((l_h, r_h));

