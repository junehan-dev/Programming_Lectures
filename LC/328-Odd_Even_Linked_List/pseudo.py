def next_odd_even(odd, even):
    """
    KEEP ODD_HEAD  = 1
    KEEP EVEN_HEAD = 2
    (1:ODD LINK HEAD),  (2:EVENLINK HEAD)

    SET ODD = 1
    SET EVEN = 2
    WHILE EVEN.NEXT:
        SET ODD, EVEN = 
            NEXT_ODD_EVEN(ODD_EVEN)

        IF NOT EVEN AND NOT EVEN.NEXT:
            RETURN (ODD_HEAD, EVEN_HEAD)
    
    next_odd_even(1,2) -> (3, 4)
    
    """
    ret_odd = even_prev.next;
    ret_prev = None;

    odd_prev.next = odd_cur; #1->3
    if cur.next:
        even_prev.next = cur.next; #2
        return (cur, cur.next)
    else:
        return (cur, None);
    if odd_cur.next:
        even_prev.next = odd_cur.next #2->4 
    return (even_prev, odd_cur) #2, 3
