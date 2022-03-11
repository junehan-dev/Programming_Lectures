from typing import List, Tuple
from doctest import testmod

class Solution:
	def	arrayPairSum(self, nums: List[int]) -> int:
		"""summation on last iterable in argument, nums.
		>>> s = Solution();
		>>> s.arrayPairSum([1,2,3,4])
		7
		"""
		paired_arr = pairArray(nums);
		return sum(paired_arr[-1]);

def pairArray(nums: List[int]) -> Tuple[Tuple[int]]:
	"""pairs an array, produce a zipped tuple with even's with odd's in nums.
	>>> pairArray([1,2,3,4]);
	((1, 2), (3, 4))
	"""
	return tuple(zip(nums[::2], nums[1::2]));

if __name__ == "__main__":
	testmod();
"""
	partition = Solution();
	ret = partition.pairArray([1,2,3,4,5,6,7,8])
	print(ret);
"""
