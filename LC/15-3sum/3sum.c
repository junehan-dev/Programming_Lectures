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
	int			ret;

	assert(argc == 2);
	in = argv[1];
	out = str_substr_max(in);
	ret = substr_len(out);
//
	write(1, "MAX:", 4);
	write(1, out, substr_len(out));
//
	return (ret);
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
		next = cur + substr_len(cur);
		cur_len = next - cur;
//
		write(1, cur, cur_len);
		write(1, ":checked\n", 9);
//
		if (cur_len > long_len) {
			long_len = cur_len;
			longest = cur;
		}
		cur++;
	}

	return (longest);
}

size_t		substr_len(const char *start)
{
	char		dict[ASCCNT] = {0};
	const char	*end;
	char		found;
	
	end = start;
	while ((found = *end) && dict[found] == 0) {
		dict[found]++;
		end++;
	}

	return (end - start);
}
