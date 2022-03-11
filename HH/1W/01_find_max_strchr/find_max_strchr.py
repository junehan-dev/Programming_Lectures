import sys

def find_max_strchr(s:str):
	keys = tuple(set(s));
	occurs = tuple(map(lambda c: s.count(c), keys));
	max_occur = max(occurs);
	idx = occurs.index(max_occur);
	ch = keys[idx];
	return (ch, max_occur);

def main(s = "hello, this is ssssparta"):
	if len(sys.argv) == 2:
		s = sys.argv[1];
	print(s);
	return (find_max_strchr(s));

if __name__ == "__main__":
	key, time = main()
	print(key, time)
	
