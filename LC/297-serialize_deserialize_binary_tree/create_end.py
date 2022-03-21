from collections import deque
from tree_node import TreeNode

def create_tree_2(data_arr):
    if not data_arr:
        return [];

    i = 0;
    max_idx = len(data_arr) - 1;
    work_q = deque();
    root = TreeNode(data_arr[i]);
    work_q.append(root);

    while work_q:
        l_idx = i * 2 + 1;
        r_idx = i * 2 + 2;
        left_v = data_arr[l_idx];
        right_v = data_arr[r_idx] if r_idx <= max_idx else None; 

        if r_idx <= max_idx:
            right_v = data_arr[r_idx];

        if left_v or right_v:
            node = work_q.popleft();
            if left_v:
                node.left = TreeNode(left_v);
                if is_leaf_valid(data_arr, l_idx, max_idx):
                    work_q.append(node.left);
            if right_v:
                node.right = TreeNode(right_v);
                if is_leaf_valid(data_arr, r_idx, max_idx):
                    work_q.append(node.right);
        i += 1;
    return (root);

def is_leaf_valid(data_arr, idx, max_idx):
    l = idx * 2 + 1;
    r = idx * 2 + 2; 

    if l <= max_idx and data_arr[l]:
        return True;
    if r <= max_idx and data_arr[r]:
        return True;
    return False;

def resolve_tree_2(node: TreeNode) -> list:
    data = [];
    if not node:
        return data;
    work_q = deque();
    root = node;
    work_q.append((root, 0));
    
    while work_q:
        node, idx = work_q.popleft();
        offset = idx - len(data);
        data += ([None] * offset);
        if node.left:
            work_q.append((node.left, idx * 2 + 1));
        if node.right:
            work_q.append((node.right, idx * 2  + 2));
        if not work_q:# 마지막 수정분
            while data[-1] == None:
                data.pop();
        data.append(node.val);
                
    return (data);

