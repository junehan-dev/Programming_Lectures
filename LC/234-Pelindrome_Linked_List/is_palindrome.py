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
        # pelindrome을 판별하기 위해서 알아야하는 정보
        # - 노드 연결수:                좌우 대칭의 중앙을 알기 위해서
        # - 각 노드의 데이터의 값:      대칭되는 부분의 값을 기준으로 비교

        # linked list의 HEAD->END까지 접근해서 모든 val을 가져와서
        value_list = nodetolist(head); # O(n)

        result = is_palindrome(value_list); # linked list가 아닌 data에 대한 O(n)
        # list의 데이터를 palinedrome인지 체크하는 함수

        return (result);


def is_palindrome(vals):
    l_idx = 0;
    r_idx = len(vals) - 1;

    while l_idx <= r_idx:
        if vals[l_idx] != vals[r_idx]:
            return False;
        l_idx += 1;
        r_idx -= 1;
    return True;

def nodetolist(node):
    to_arr = [];
    head = node;
    while node:
        to_arr.append(node.val);
        node = node.next;
    return (to_arr);

def recursive_nodetolist(node):
    if node.next is None:
        return [node.val];
    return ([node.val] + recur_nodetolist(node.next));

if __name__ == "__main__":
    a_sol = Solution();
    arr = [1, 2, 1];
    node = ListNode.make_link(arr);
    assert(node.val == arr[0]);
    assert(node.next.val == arr[1]);
    assert(node.next.next.val == arr[2]);
    assert(node.next.next.next is None);
    print(arr, "is Palindrome? :	", a_sol.isPalindrome(node));

    arr = [1, 1];
    node = ListNode.make_link(arr);
    print(arr, "is Palindrome? :	", a_sol.isPalindrome(node));

    arr = [1, 2];
    node = ListNode.make_link(arr);
    print(arr, "is Palindrome? :\t", a_sol.isPalindrome(node));

    arr = [1, 2, 2, 2];
    node = ListNode.make_link(arr);
    print(arr, "is Palindrome? :\t", a_sol.isPalindrome(node));

    arr = [1, 2, 2, 1];
    node = ListNode.make_link(arr);
    print(arr, "is Palindrome? :\t", a_sol.isPalindrome(node));

    arr = [1];
    node = ListNode.make_link(arr);
    print(arr, "is Palindrome? :\t", a_sol.isPalindrome(node));


