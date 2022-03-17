#include <assert.h>
#include <unistd.h>
#define ASCII_MAX 128

const char	*str_substr_max(const char *in);
size_t		substr_len(const char *s);
const char	*next_substr(const char *s);

int	main(int argc, const char *argv[])
{
	const char *in;
	const char *out;
	int			out_len;

	assert(argc == 2);
	in = argv[1];
	out = str_substr_max(in);
	out_len = substr_len(out);
//
	write(1, "MAX:", 4);
	write(1, out, out_len);
//
	return (out_len);
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

size_t		substr_len(const char *s)
{
	char		dict[ASCII_MAX] = {0};
	const char	*s_end;
	char		ch;
	
	s_end = s;
	while ((ch = *s_end) && dict[ch] == 0) {
		dict[ch]++;
		s_end++;
	}

	return (s_end - s);
}
