from collections import Counter;
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [None] * k;
        counter = 0;
        base = 1;
        set_count = 0;

        i = 0;
        nums.append(None);
        while (nums[i] != None):
            if nums[i] == base:
                counter += 1;
            else:
                if set_count < k:
                    freq_map[set_count] = (base, counter); #UpDATE
                else:
                    least_idx, least_value = find_least_freq(freq_map);
                    if counter > least_value:
                        freq_map[least_idx][0] = base;
                        freq_map[least_idx][1] = counter;
                    #else:
                        #pass DO NOTHING
                base = nums[i];
                counter = 1;
                set_count += 1;
            i += 1;

        return (list(map(lambda el: el[0], freq_map)));

def find_least_freq(freq_map):
    least_counter = freq_map[0][1];
    least_idx = 0;

    for i, freq_set in enumerate(freq_map):
        _, counter = freq_set;
        if counter < least_counter:
            least_idx = i
            least_counter = counter;

    return (least_idx, least_counter);
    
if __name__ == "__main__":
    a_sol = Solution();

    data = [1,1,1,3,3,4,5,6];
    ret = a_sol.topKFrequent(data, 3);
    
    print(ret);
