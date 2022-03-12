from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def make_link(vals):
        *f, tail = list(map(ListNode, vals));
        while f:
            f[-1].next = tail;
            *f, tail = f;

        return (tail);

class Solution:        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = nodetolist(head);
        return (is_palindrome(vals));

def nodetolist(node):
    to_arr = [];
    head = node;
    while node:
        to_arr.append(node.val);
        node = node.next;
    return (to_arr);

def is_palindrome(vals):
    l_idx = 0;
    r_idx = len(vals) - 1;
    while l_idx <= r_idx:
        if vals[l_idx] != vals[r_idx]:
            return False;
        l_idx += 1;
        r_idx -= 1;

    return True;

if __name__ == "__main__":
    arr = [1, 2, 1];
    node = ListNode.make_link(arr);
    a_sol = Solution();
    print(a_sol.isPalindrome(node));
