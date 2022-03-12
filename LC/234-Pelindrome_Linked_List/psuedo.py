from typing import Optional
# Definition for singly-linked list.
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
        
    def isPalindrome(self, head) -> bool:
        pass

def nodetolist(node):
    to_arr = [];
    head = node;
    while node:
        to_arr.append(node.val);
        node = node.next;
    return (to_arr);

def is_palindrome(vals):
    r_idx = len(vals);
    if r_idx % 2:
        return False;

    l_idx = 0;
    r_idx -= 1;
    while l_idx < r_idx:
        if vals[l_idx] != vals[r_idx]:
            return False;
        l_idx += 1;
        r_idx -= 1;
    return True;

if __name__ == "__main__":
    node = ListNode.make_link([1,2,2,1]);
    while node:
        print("cur: ", node.val);
        temp = node.next;
        del(node);
        node = temp;
        del(temp);
    arr = [1,2,2,1];
    print(is_palindrome(arr));
