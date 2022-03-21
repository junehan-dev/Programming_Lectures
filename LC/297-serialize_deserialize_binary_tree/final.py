# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = resolve_tree_2(root);
        to_str = list(map(lambda el: f"{el}" if el is not None else "null", ret));
        ret = ",".join(to_str)
        return (ret);
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        to_list = list(data.split(','));
        print(to_list)
        to_list = list(filter(lambda el: el == "null" or el, to_list));
        to_tree_data = list(map(lambda el: None if el == "null" else int(el), to_list));
        ret = create_tree_2(to_list);
        return (ret);
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

from collections import deque
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
        if l_val is not None:
            node.left = TreeNode(l_val);
            work_q.append(node.left);
        if r_val is not None:
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
                data.append(node.left.val);
                work_q.append(node.left);
            if not node.left:
                data.append(None);
            if node.right:
                data.append(node.right.val);
                work_q.append(node.right);
            if not node.right:
                if work_q:
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

