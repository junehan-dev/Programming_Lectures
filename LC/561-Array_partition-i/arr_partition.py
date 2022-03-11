from typing import List, Tuple
from functools import reduce

class Solution:
	def	arrayPairSum(self, nums: List[int]) -> int:
		sorted_nums = sorted(nums);
		odd_idx_nums = sorted_nums[::2];
		return sum(odd_idx_nums);

def sortArray(nums: List[int]) -> List[int]:
	return (sorted(nums));

def sliceEven(nums: List[int]) -> List[int]:
	return (nums[::2]);

if __name__ == "__main__":
	a_sol = Solution()
	print(a_sol.arrayPairSum([1,2,3,4]));
