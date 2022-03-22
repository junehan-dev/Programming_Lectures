from tree_node import TreeNode
from collections import deque

def create_tree(py_list_data):
    if not py_list_data:
        return [];
    work_q          = deque();
    serial_queue    = deque(py_list_data);
    root            = TreeNode(serial_queue.popleft());

    work_q.append(root);

    while len(serial_queue):
        node            = work_q.popleft();
        left_value      = serial_queue.popleft();
        right_value     = serial_queue.popleft() if serial_queue else None;

        if left_value is not None:
            node.left   = TreeNode(left_value);
            work_q.append(node.left);

        if right_value is not None:
            node.right  = TreeNode(right_value);
            work_q.append(node.right);

    return (root); 

