#include <assert.h>
#include <unistd.h>
#define ASCCNT 128

const char	*str_substr_max(const char *in);
size_t		substr_len(const char *s);
const char	*next_substr(const char *s);

int	main(int argc, const char *argv[])
{
	const char *in;
	const char *out;

	assert(argc == 2);
	in = argv[1];
	out = str_substr_max(in);
	write(1, out, substr_len(out));
	return (0);
}

const char *str_substr_max(const char *in)
{
	const char	*cur;
	const char	*next;
	const char	*longest;
	size_t		cur_len;
	size_t		long_len;


	long_len = 0;
	cur = in;
	longest = cur;
	while (*cur) {
		next = next_substr(cur);
		cur_len = next - cur;
		write(1, cur, cur_len);
		write(1, ":cur\n", 5);
		if (cur_len > long_len) {
			long_len = cur_len;
			longest = cur;
		}
		cur++;
	}

	return (longest);
}

const char	*next_substr(const char *start)
{
	return (start + substr_len(start));
}

size_t		substr_len(const char *start)
{
	char		dict[ASCCNT] = {0};
	const char	*end;
	char		found;
	
	end = start;
	write(1, "substr_len()\n", 13);
	while ((found = *end) && dict[found] == 0) {
		dict[found]++;
		end++;
	}

	return (end - start);
}
