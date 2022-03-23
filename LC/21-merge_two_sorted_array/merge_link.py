def merge_link(h1, h2):
    """Merge 2 linked list.

    - head of link
       expect head has smallest value.
    - links from head to tail
       they have values ascending, compared to head of them.
    """
    if not (h1 or h2):
        return None;

    stack = [];
    while (h1 and h2):
        if h1.val < h2.val:
            stack.append(h1);
            h1 = h1.next;
        else:
            stack.append(h2);
            h2 = h2.next;

    left = h1 if h1 else h2
    while left:
        stack.append(left);
        left = left.next; # last next will be none but not is the stack.

    head = stack.pop() if stack else None;
    
    if len(stack):
        tail = head;
        head = prepend_nodes(tail, stack);

    return (head);

def prepend_nodes(tail, stack):
    """pop off the stack and link

    - DESC
       like pop3->pop2->pop1->tail
    """
    head = stack.pop(); 
    while stack:
        head.next = tail;
        tail = head;
        head = stack.pop();
    head.next = tail;

    return (head);
