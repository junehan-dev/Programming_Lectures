from typing import List

class Solution:
	def	arrayPairSum(self, nums: List[int]) -> int:
		nums.sort();
		return sum(nums[::2]);

if __name__ == "__main__":
	a_sol = Solution()
	print(a_sol.arrayPairSum([1,2,3,4]));
