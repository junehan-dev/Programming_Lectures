#include <unistd.h>
#include <string.h>

int		itoa(char buf[], int n);
int		get_num(void);
void	count_primes(int start, int end);

int		main()
{
	int		start;
	int		end;

	start = get_num();
	end = get_num();
	count_primes(start, end);
	return (0);
}

void	count_primes(int start, int end) {
	char	primes[1000001] = {0};
	char	buf[8];
	int		i;
	int		buflen;
	int		mul;

	if (end == 1)
		return ;
	if (end == 2) {
		write(STDOUT_FILENO, "2", 2);
		return ;
	}

	i = 3;
	while (i < 50000) {
		if (!primes[i]) {
			mul = 2;
			while (i * mul <= 1000000)
				primes[i * mul++] = 1;
		}
		i += 2;
	}

	buf[0] = 0;
	if (start <= 2) 
		write(STDOUT_FILENO, "2\n", 2);
	start = start == 1 ? 3 : start;
	start = start % 2 ? start : start + 1;
	while (start <= end) {
		if (!primes[start]) {
			if (buf[0])
				write(STDOUT_FILENO, buf, buflen + 1);
			buflen = itoa(buf, start);
			buf[buflen] = '\n';
		}
		start += 2;
	}

	if (buf[0])
		write(STDOUT_FILENO, buf, buflen);
}

int itoa(char *dest, int n)
{
	int	div;
	int i;
   
	div = 1000000;
	while (!(n / div))
		div /= 10;

	i = 0;
	while (div) {
		dest[i++] = n / div + '0';
		n %= div;
		div /= 10;
	}

	return (i);
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


