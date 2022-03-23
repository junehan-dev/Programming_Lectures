from tree_node import TreeNode

class HeightBalanceError(Exception):
    """Raised When the height of tree differ more than one."""
    pass

def is_balanced(t):
    if not t:
        return True;
    try:
        dfs_height(t);
    except HeightBalanceError as e:
        return False;
    return True;

def dfs_height(root: TreeNode) -> bool:
    l_h = (1 + is_balanced(root.left)) if root.left else None;
    r_h = (1 + is_balanced(root.right)) if root.right else None;

    if not any((l_h, r_h)):
        return (0);

    l_h = l_h if l_h is not None else r_h;
    r_h = r_h if r_h is not None else l_h;

    if abs(l_h - r_h) > 1:
        raise HeightBalanceError(f"{root}.left: {l_h}, right: {r_h}. non matched height found.");
    return max((l_h, r_h));
 
