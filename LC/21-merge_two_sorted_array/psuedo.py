from collections import deque
from typing import Optional
from s_linked_list_node import Node as ListNode

class Solution:
    def mergeTwoLists(self, s1: Optional[ListNode], s2: Optional[ListNode]) -> Optional[ListNode]:
        pass   

def start():
    s1 = ListNode.make_sequence([1,2,3]);
    s2 = ListNode.make_sequence([1,3,4]);
    return merge_link(s1, s2);

"""
            s1, [1] -> [2] -> [3]
            s2, [1] -> [3] -> [4]
"""
def merge_link(h1, h2):
    stack = [];
    while (h1 and h2):
        if h1.val < h2.val:
            stack.append(h1);
            h1 = h1.next;
        else:
            stack.append(h2);
            h2 = h2.next;

    h = h1 if h1 else h2
    while h:
        stack.append(h);
        h = h.next;
    assert(not all([h1, h2]));
    #FIN PUSH
    
    for node in stack:
        print(node.val);
    #STACK pop link
    head = stack.pop();
    if len(stack) > 1:
        poped = stack.pop();
        while stack:
            poped.next = head;
            head = poped;
            poped = stack.pop();
    return (head);

if __name__ == "__main__":
    head = start();
    #print("FIN");
    #while(head):
        #print(head.val);
        #head = head.next
