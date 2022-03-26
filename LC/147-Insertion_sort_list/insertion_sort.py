from nodes import Node

def insertion_sort(head):
    if (head.next is None):
        return (head);

    base_node = Node(None); # 1. None -> head
    base_node.next = head;
    cur = base_node.next;   # 2. cur = head;
    while (cur.next is not None): # 1 -> n
        if (cur.val <= cur.next.val): # skip ASCENDING ORDER
            cur = cur.next;
        else:
            insert_node = cur.next;
            cur.next = insert_node.next;
            prev_node = base_node; # from 0 -> (cur.prev)
            next_node = prev_node.next; # from 1 -> (cur)
            while (next_node.val < insert_node.val): # skip ASC
                prev_node = next_node;
                next_node = next_node.next;
            prev_node.next = insert_node; # prev -> (NEW)
            insert_node.next = next_node; # (NEW) -> next
 
    return (base_node.next);

