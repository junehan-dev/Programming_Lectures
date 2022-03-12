from typing import Optional
from node import Node as ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

if __name__ == "__main__":
    data = [1,2,3,4,5];
    head = ListNode.make_sequence(data);
    a_sol = Solution();
    odd_even_sorted = a_sol.oddEvenList(head);

    node = head;
    while node.next:
        print(node);
        node = node.next

    print(node);

