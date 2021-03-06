from tree_node import TreeNode
from collections import deque

class Codec:
    def serialize(self, root):
        py_list_data    = resolve_tree(root);
        to_str          = list(map(
            lambda data: f"{data}" if data is not None else "null",
            py_list_data
            )
        );
        ret             = ",".join(to_str)
        return (ret);
        
    def deserialize(self, data):
        py_list_data    = list(map(
            lambda el: None if el == "null" else int(el),
            data.split(',')
            )
        );
        ret             = create_tree(py_list_data);
        return (ret);

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

