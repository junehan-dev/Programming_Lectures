from tree_node import TreeNode
from collections import deque

class Codec:
    def serialize(self, root):
        py_list_data    = resolve_tree(root);
        to_str          = list(map(lambda el: f"{el}" if el is not None else "null", py_list_data));
        ret             = ",".join(to_str)
        return (ret);
        
    def deserialize(self, data):
        py_list_data    = list(map(lambda el: None if el == "null" else int(el), data.split(',')));
        ret             = create_tree(py_list_data);
        return (ret);



def create_tree(data_arr):
    if not data_arr:
        return [];
    work_q          = deque();
    serial_queue    = deque(data_arr);
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
    data        = [];
    work_q      = deque();
    root        = node;

    work_q.append(root);
    data.append(node.val);

    while work_q:
        node = work_q.popleft();

        if node.left and node.right:
            data.append(node.left.val);
            work_q.append(node.left);
        elif node.left:
            data.append(node.left.val);
            work_q.append(node.left);
            if work_q:
                temp_q = list(work_q);
                if is_left(temp_q):
                    data.append(None);
        elif node.right:
            data.append(None);
            if node.right:
                data.append(node.right.val);
                work_q.append(node.right);
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

