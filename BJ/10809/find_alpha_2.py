def find_alpha_2(s:str):
	ret = "";
	s_to_int = tuple(map(ord, s));
	start = ord('a');
	end = ord('z');
	
	for i in range(end - start):
		try:
			ret += f"{s_to_int.index(start + i)}"
		except ValueError:
			ret += "-1"
		finally:
			ret += " "

	ret += f"{s_to_int.index(start + i)}" if end in s_to_int else "-1"

	return (ret);

