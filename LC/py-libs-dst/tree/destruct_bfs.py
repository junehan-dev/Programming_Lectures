from tree_node import TreeNode
from collections import deque

def resolve_tree(node: TreeNode) -> list:
    if not node:
        return [];

    serial_data = [];
    work_q      = deque();
    root        = node;

    work_q.append(root);
    while any(work_q):
        node = work_q.popleft();
        if node is None:
            serial_data.append(None);
        else:
            serial_data.append(node.val)
            work_q.append(node.left);
            work_q.append(node.right);
    return (serial_data);

