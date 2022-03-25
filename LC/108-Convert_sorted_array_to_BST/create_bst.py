from tree_node import TreeNode

def create_bst_dsf(sorted_arr):
    assert(sorted_arr);
    root = TreeNode(sorted_arr[len(sorted_arr) // 2]);
    dfs_recursion(root, sorted_arr) if len(sorted_arr) > 1 else None;
    return root;

def dfs_recursion(parent, sorted_arr):
    if len(sorted_arr) < 2:
        return None;

    mid = len(sorted_arr) // 2;
    l_arr = sorted_arr[:mid];
    parent.left = TreeNode(l_arr[len(l_arr) // 2]);
    dfs_recursion(parent.left, l_arr);
    r_arr = sorted_arr[mid+1:];
    if r_arr:
        parent.right = TreeNode(r_arr[len(r_arr) // 2]);
        dfs_recursion(parent.right, r_arr);

def dfs_recursion2(arr):
    mid = len(arr) // 2;
    parent = TreeNode(arr[mid]);
    parent.left = dfs_recursion(arr[:mid]) if mid else None;
    parent.right = dfs_recursion(arr[mid + 1:]) if len(arr) > 2 else None;
    return parent;

from collections import deque

def create_bst_bfs(sorted_arr):
    assert(sorted_arr);
    root = TreeNode(sorted_arr[len(sorted_arr) // 2]);
    q_subtree = deque([(root, sorted_arr)]);

    while q_subtree:
        parent, sorted_arr = q_subtree.popleft();
        left = len(sorted_arr);
        mid = left // 2;

        if left > 1:
            l_arr = sorted_arr[:mid];
            parent.left = TreeNode(l_arr[len(l_arr) // 2]);
            q_subtree.append((parent.left, l_arr));
        if left > 2:
            r_arr = sorted_arr[mid+1:];
            parent.right = TreeNode(r_arr[len(r_arr) // 2]);
            q_subtree.append((parent.right, r_arr));

    return root;

