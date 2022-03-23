from tree_node import TreeNode

class HeightBalanceError(Exception):
    """Raised When the height of tree differ more than one."""
    pass

def is_balanced(t):
    try:
        dfs_height(t);
    except ValueError as e:
        return False;
    return True;

def dfs_height(root: TreeNode) -> bool:
    if not all([root.left, root.right]):
        return (0);

    l_h = (1 + is_balanced(root.left)) if root.left else None;
    r_h = (1 + is_balanced(root.right)) if root.right else None;
    l_h = l_h if l_h else r_h;
    r_h = r_h if r_h else r_h;
    
    if abs(l_h - r_h) > 1:
        raise HeightBalanceError(f"l_h: {l_h}, r_h: {r_h}");

    return max((l_h, r_h));
    
