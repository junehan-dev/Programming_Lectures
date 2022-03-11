def find_alpha_3(s:str):
	s_arr = tuple(map(ord, s));
	alphabet = range(ord('a'), ord('z') + 1);
	to_index_in_s = lambda ch: f"{s_arr.index(ch)}" if (ch in s_arr) else "-1";
	ret = map(to_index_in_s, alphabet);
	return (" ".join(ret));

if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		ret = find_alpha_3(sys.argv[1]);
		print(ret);
