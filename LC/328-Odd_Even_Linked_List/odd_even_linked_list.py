from typing import Optional
from node import Node as ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not isinstance(head, ListNode):
            return (head);

        even_head = head.next;
        if even_head is None or even_head.next is None:
            return (head);

        odd_end = head;
        even_end = even_head;
        while even_end is not None and even_end.next is not None: # 3?
            odd_end, even_end = next_odd_even(odd_end, even_end);
        odd_end.next = even_head;
        return (head);

def next_odd_even(odd, even):
    cur = even.next; # cur = 3
    odd.next = cur; # 1 -> 3
    even.next = cur.next; # 2 -> 4? or None
    return (cur, cur.next); # 3, 4?or None
    
        
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6];
    head = ListNode.make_sequence(data);
    a_sol = Solution();
    odd_even_sorted = a_sol.oddEvenList(head);
    node = head;
    while node.next:
        print(node);
        node = node.next
    print(node);

