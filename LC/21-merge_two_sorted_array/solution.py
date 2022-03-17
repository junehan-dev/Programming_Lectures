from collections import deque
from typing import Optional
from s_linked_list_node import Node as ListNode

class Solution:
    def mergeTwoLists(self, s1: Optional[ListNode], s2: Optional[ListNode]) -> Optional[ListNode]:
        ret: Optional[ListNode];
        if all([s1, s2]):
            ret = merge_link(s1, s2);
        else:
            ret = s1 if s1 else s2;
        return (ret);

def merge_link(h1, h2):
    stack = [];
    while (h1 and h2):
        if h1.val < h2.val:
            stack.append(h1);
            h1 = h1.next;
        else:
            stack.append(h2);
            h2 = h2.next;
#    [print(node.val) for node in stack];
    h = h1 if h1 else h2
    assert(h.val)
    while h:
        stack.append(h);
        h = h.next;
    assert(not h);
    #FIN PUSH
    #STACK pop link
    head = stack.pop();
    if len(stack) > 1:
        poped = stack.pop();
        while stack:
            poped.next = head;
            head = poped;
            poped = stack.pop();
        poped.next = head;
        head = poped;
    return (head);

def debug_node(head):
    while head:
        print("head: ",head.val);
        head = head.next;

if __name__ == "__main__":
    a_sol = Solution();

    arr1 = [1,2,3]
    arr2 = [3,4,5]

    s1 = ListNode.make_sequence(arr1);
    s2 = ListNode.make_sequence(arr2);

    debug_node(a_sol.mergeTwoLists(s1, s2));
