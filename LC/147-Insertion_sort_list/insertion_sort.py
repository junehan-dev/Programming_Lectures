from nodes import Node

def insertion_sort(head):
    if (head.next is None):
        return (head);

    base_node = Node(None);
    base_node.next = head;
    cur = base_node.next;
    while (cur.next):
        target_node = cur.next;
        if (cur.val > target_node.val):
            cur.next = target_node.next;
            prev_node = base_node;
            cmp_node = base_node.next;
            while (cmp_node.val < target_node.val):
                prev_node = cmp_node;
                cmp_node = cmp_node.next;
            prev_node.next = target_node;
            target_node.next = cmp_node;
        else:
            cur = target_node;
    
    return (base_node.next);


