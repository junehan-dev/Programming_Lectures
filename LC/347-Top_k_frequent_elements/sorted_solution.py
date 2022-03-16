from collections import Counter;
from typing import List

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mosts = Counter(nums).most_common(k);
        return [key for key, _ in mosts]
"""

# if no good builtins..
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [];
        counter = 0;
        base = nums[0];
        set_count = 0;
        nums.append(None);
        i = 0;
        
        while (nums[i] != None):
            if nums[i] == base:
                counter += 1;
            else:
                if set_count < k:
                    freq_map.append((base, counter)); #UpDATE
                else:
                    least_idx, least_counter = find_least_freq(freq_map);
                    if counter > least_counter:
                        freq_map[least_idx] = (base, counter);
                print("next:", nums[i]);
                base = nums[i];
                counter = 1;
                set_count += 1;
            i += 1;

        if not freq_map or set_count < k:
            freq_map.append((base, counter));
        else:
            least_ids, least_counter = find_least_freq(freq_map);
            if counter > least_counter:
                freq_map[least_idx] = (base, counter);

        return (list(map(lambda el: el[0], freq_map)));


def find_least_freq(freq_map):
    least_counter = freq_map[0][1];
    least_idx = 0;
    for i, freq_set in enumerate(freq_map):
        if not freq_set:
            return (i, 0)
        _, counter = freq_set;
        if counter < least_counter:
            least_idx = i
            least_counter = counter;

    return (least_idx, least_counter);
    
if __name__ == "__main__":
    a_sol = Solution();

    data = [1,1,1,3,3,4,5,6];
    #ret = a_sol.topKFrequent(data, 3);

    data = [1];
    #ret = a_sol.topKFrequent(data, 1);
    
    data = [1,2];
    #ret = a_sol.topKFrequent(data, 2);

    data = [3, 0, 1, 0];
    ret = a_sol.topKFrequent(data, 1);
    print(ret);
