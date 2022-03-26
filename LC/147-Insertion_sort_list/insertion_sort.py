from nodes import Node

def insertion_sort(head):
    if (head.next is None):
        return (head);

    base_node = Node(None); # 1. None -> head
    base_node.next = head;
    cur = base_node.next;   # 2. cur = head;
    while (cur.next is not None):
        if (cur.val <= cur.next.val):
            cur = cur.next;
        else: # cur.val > cur.next.val
            target = cur.next;
            cur.next = target.next;
            prev_node = base_node;
            cmp_node = base_node.next;
            while (cmp_node.val < target.val):
                prev_node = cmp_node;
                cmp_node = cmp_node.next;
            # prev_node.val < target.val < cmp_node.val
            prev_node.next = target;
            target.next = cmp_node;
    
    return (base_node.next);


