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
    serial_data.append(node.val);

    while work_q:
        node = work_q.popleft();

        if node.left and node.right:
            register_node(serial_data, work_q, node.left);
            register_node(serial_data, work_q, node.right);
        elif node.left and not node.right:
            register_node(serial_data, work_q, node.left);
            if is_lower_level(work_q):
                serial_data.append(None);
        elif node.right and not node.left:
            serial_data.append(None);
            if node.right:
                serial_data.append(node.right.val);
                work_q.append(node.right);
        else:
            temp_q = list(work_q);
            if is_lower_level(temp_q):
                serial_data.append(None);
                serial_data.append(None);
    return (serial_data);


def register_node(serial_data, work_q, node):
    serial_data.append(node.val);
    work_q.append(node);

def is_lower_level(nodes):
    for n in nodes:
        if n.left or n.right:
            return True;
    return False;


