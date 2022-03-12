class Solution:
    def mergeTwoLists(self, s1: Optional[ListNode], s2: Optional[ListNode]) -> Optional[ListNode]:
        pass

def partion_less(s1, s2):
    here = 0;
    there = 0;

    if s1[here] <= s2[there]:
        while s2 and s1[here] <= s2[there]:
            there += 1;
        s1 = s2[:there] + s1[here:]
        s2 = s2[there:]    
        return (s1, s2)
    else:
        while s1[here] > s2[there]:
            here += 1;

