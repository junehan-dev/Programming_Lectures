#include <unistd.h>

int	is_dividable(int n);
int	get_mindiv(int n);
int	main(void)
{
	char	buf[5] = {0};
	int		i;
	int		n;
	int		div;
	char	key;

	i = 0;
	n = 0;

	while (read(STDIN_FILENO, &key, 1) && 0 <= key - '0' && key -'0' < 10)
		buf[i++] = key;

	i = 0;
	while (buf[i]) {
		n *= 10;
		n += (buf[i++] - '0');
	}

	if (!is_dividable(n)) {
		write(1, "-1", 2);
	} else {
		n = get_mindiv(n);
		div = 1000;
		while (!(n / div))
			div /= 10;

		i = 0;
		while (div) {
			buf[0] = (n / div) + '0';
			write(1, buf, 1);
			n %= div;
			div /= 10;
		}
	}

	return (0);
}

int	is_dividable(int n)
{
	if (n == 7 || n == 4)
		return (0);

	return (1);
}

int	get_mindiv(int n)
{
	int	ret;

	if (n < 11) {
		if (!(n % 3)) {
			return (n / 3);
		} else if (!(n % 5)) {
			return (n / 5);
		} else {
			return (2);
		}
	}
	n -= 1;
	ret = n / 5 + 1;
	n %= 5;
	return ((n & 1) ? ret + 1 : ret);
}

