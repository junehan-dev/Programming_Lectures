from typing import Optional
from node import Node as ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not isinstance(head, ListNode) or head.next == None:
            return (head);

        tail = head;
        while tail.next:
            tail = tail.next
        assert(reverse_traverse(head, link) == head);
        return (tail)

def reverse_traverse(head, cb):
    if head.next:
        tail = reverse_traverse(head.next, cb)
        cb(tail, head);
        return (head);
    return head;

def link(head, tail):
    head.next = tail;
    tail.next = None;


def iterative_reverse(head):
    if not isinstance(head, ListNode) or head.next is None:
        return (head);

    stack = [];

    while head.next:
        stack.append(head);
        head = head.next;

    ret = head;
    while stack:
        tail = stack.pop()
        head.next = tail;
        head = tail;
    head.next = None;

    return (ret);

if __name__ == "__main__":
    data = [1,2,3,4,5];
    head = ListNode.make_sequence(data);
    print("RECURESION");

    a_sol = Solution();
    reversed_head = a_sol.reverseList(head);
    
    print(reversed_head);
    tail = reversed_head.next;
    while tail.next:
        print(tail);
        tail = tail.next

    print(tail);
    assert(tail.next is None);
    
    print("ITERATIVES");
    head = iterative_reverse(reversed_head);
    
    print(head);
    tail = head.next;
    while tail.next:
        print(tail);
        tail = tail.next

    print(tail);
    assert(tail.next is None);

