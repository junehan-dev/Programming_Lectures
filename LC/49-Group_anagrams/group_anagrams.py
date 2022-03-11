from typing import List
from collections import Counter

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		ret = [];
		while strs:
			cmp, *strs = strs;
			idx_arr = get_anagrams(strs, cmp);
			ret += [[cmp ] + list(map(lambda i: strs[i], idx_arr))];
			strs = [v for i, v in enumerate(strs) if i not in idx_arr];
		return ret;

def	get_anagrams(strs, cmp):
	cmp = Counter(cmp);
	return [i for i, v in enumerate(list(map(Counter, strs))) if v == cmp];

if __name__ == "__main__":
	strs = "eat,tea,tan,ate,nat,bat".split(",");
	strs.append("");
	strs.append("");
	strs.append("");
	expect = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];
	a_sol = Solution();
	ret = a_sol.groupAnagrams(strs);
	print(ret);
	strs = "dddddt,tttttd".split(",");
	ret = a_sol.groupAnagrams(strs);
	print(ret);
