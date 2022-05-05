#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char    *itoa(int n);
int		get_num(void);
int		count_primes(int n);

int		main()
{
	char	*s;
	int		n;
	char	buf[BUFSIZ];
	char	*buf_pt;

	buf_pt = buf;
	while ((n = get_num())) {
		s = itoa(count_primes(n));
		strcpy(buf_pt, s);
		buf_pt += strlen(s);
		free(s);
		*buf_pt++ = '\n';
	}

	*(buf_pt - 1) = '\0';
	write(STDOUT_FILENO, buf, strlen(buf));

	return (0);
}

int count_primes(int n) {
	static int	primes[246913];
	int			i;
	int			mul;
	int			ret;

	if (!primes[0]) {
		primes[0] = 1;
		primes[1] = 1;
		primes[246912] = 1;
		i = 1;
		while (i < 123456) {
			if (!primes[++i]) {
				mul = 2;
				while (i * mul < 246913)
					primes[i * mul++] = 1;
			}
		}
	}

	i = n;
	ret = 0;
	while (i++ < n * 2)
		ret = !primes[i] ? ret + 1: ret;

	return (ret);
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

