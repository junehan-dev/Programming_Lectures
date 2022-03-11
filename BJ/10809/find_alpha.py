import sys
import string

def find_alpha(s:str):
	s_to_int = tuple(map(ord, s));
	start = ord('a');
	end = ord('z');
	
	for i in range(end - start):
		try:
			print(s_to_int.index(start + i), end = " ");
		except ValueError:
			print("-1", end = " ");
	try:
		print(s_to_int.index(end), end = "");
	except ValueError:
		print("-1", end = "");

if __name__ == "__main__":
	if len(sys.argv) == 2:
		find_alpha(sys.argv[1]);
