from collections import deque
from functools import reduce

class TreeNode(object):
    def __init__(self, v):
        self._v = v
        self.left = None
        self.right = None

    @property
    def val(self):
        return self._v;

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


def bfs(tree, target):
    q = deque();
    q.append((tree, 0));
    ret = 0;
    while q:
        node, log = q.popleft();
        if node.left and node.right:
            q.append((node.left, log + node.val));
            q.append((node.right, log + node.val));
        else:
            if log + node.val == target:
                ret += 1;
    return ret;
       
def dfs_traverse(t, log, target):
    if not t.left and not t.right:
        ret = sum(log)+ t.val;
        if ret == target:
            return 1;  
        return 0
    ret = 0;
    if t.left:
        ret += dfs_traverse(t.left, log + [t.val], target);
    if t.right:
        ret += dfs_traverse(t.right, log + [t.val], target);
    return ret;

def solution(numbers, target):
    numbers = numbers;
    data = []
    for i,v in enumerate(numbers):
        to_add = [v, -v] * (2**i);
        data += to_add;
    t_data =[0] + data;
    t = create_tree(t_data);
    ret_1 = bfs(t,target);
    ret_2 = dfs_traverse(t, [], target);

    return (ret_1, ret_2);

assert(solution([1,1,1,1,1], 3) == (5, 5));
assert(solution([4,1,2,1], 4) == (2, 2));

