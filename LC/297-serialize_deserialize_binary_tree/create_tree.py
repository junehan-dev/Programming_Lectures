from collections import deque
from tree_node import TreeNode

def create_tree_2(data_arr):
    if not data_arr:
        return [];

    i = 0;
    work_q = deque();
    data_q = deque(data_arr);
    root = TreeNode(data_q.popleft());
    work_q.append(root);

    while data_q:
        node = work_q.popleft();
        l_val = data_q.popleft();
        r_val = data_q.popleft() if data_q else None;
        if l_val:
            node.left = TreeNode(l_val);
            work_q.append(node.left);
        if r_val:
            node.right = TreeNode(r_val);
            work_q.append(node.right);
    return (root); 

def is_leaf_valid(node):
    if node.left or node.right:
        return True;
    return False;

def resolve_tree_2(node: TreeNode) -> list:
    data = [];
    if not node:
        return data;
    work_q = deque();
    root = node;
    work_q.append(root);
    data.append(node.val);
    while work_q:
        node = work_q.popleft();
        if node.left or node.right:
            if node.left:
                data_q.append(node.left.val);
                work.append(node.left);
            if node.right:
                data.append(node.right.val);
                work_q.append(node.right);
            if not node.left:
                data.append(None);
            if not node.right:
                data.append(None);
        else:
            temp_q = list(work_q);
            if is_left(temp_q):
                data.append(None);
                data.append(None);
    return (data);

def is_left(nodes):
    for n in nodes:
        if n.left or n.right:
            return True;
    return False;
