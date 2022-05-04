#include <unistd.h>
#include <string.h>
#include <stdlib.h>

char    *itoa(int n);
int		get_num(void);
int		count_primes(int n);

int		main()
{
	char *s;
	int n;
	int i;

	while ((n = get_num())) {
		s = itoa(n);
		write(STDOUT_FILENO, s, strlen(s));
		free(s);
	}

	return 0;
}

char    *itoa(int n)
{
    unsigned int    left;
    char            buf[12];
    char            *buf_pt;

    if (!n)
        return (strdup("0\0"));

    *(buf+11) = 0;
    buf_pt = (buf + 10);
    left = n;
    if (n < 0)
    {
        *buf = '-';
        left = ~n + 1;
    }
    while (left >= 10)
    {
        *buf_pt-- = '0' + (left % 10);
        left /= 10;
    }
    *buf_pt = '0' + left;
    buf_pt = (*buf == '-') ? (buf_pt - 1) : buf_pt;
    if (*buf == '-')
        *buf_pt = '-';
    return (strdup(buf_pt)); 
}

int		get_num(void)
{
	char	key;
	int		ret;

	ret = 0;

	while (read(STDIN_FILENO, &key, 1) && key <= '9' && key >= '0') {
		ret *= 10;
		ret += key - '0';
	}
	return ret;
}

