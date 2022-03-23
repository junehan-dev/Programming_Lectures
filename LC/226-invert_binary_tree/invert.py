from collections import deque
from tree_node import TreeNode

def invert_tree(parent: TreeNode):
    q_subtree = deque([parent]);
    while q_subtree:
        p = q_subtree.popleft();
        swap_tree(p);
        q_subtree.append(p.left) if p.left else None;
        q_subtree.append(p.right) if p.right else None;
    return (parent);
    
def swap_tree(parent):
    temp = parent.left;
    parent.left = parent.right;
    parent.right = temp;

def invert_tree_dfs(parent: TreeNode):
    invert_tree_dfs(parent.left) if parent.left else None;
    invert_tree_dfs(parent.right) if parent.right else None;
    swap_tree(parent);
