#include <unistd.h>
#include <ctype.h>

enum CMDS	{ push = 1, pop, size, empty, top};

int		itoa(char buf[], int n);
int		get_num(void);
int		get_cmd(void);
void	read_int(int v);
int		main()
{
	int cur;
	int max;
	int	cmd;

	max = get_num();
	cur = 0;
	int stack[10000];

	while (max--) {
		switch (get_cmd()) {
			case push:
				*(stack + cur++) = get_num();
				break;
			case pop:
				(cur > 0) ? read_int(*(stack + --cur)) : write(STDOUT_FILENO, "-1\n", 3);
				break;
			case size:
				cur ? read_int(cur): write(STDOUT_FILENO, "0\n", 2);
				break;
			case empty:
				cur > 0 ? write(STDOUT_FILENO, "0\n", 2) : write(STDOUT_FILENO, "1\n", 2);
				break;
			default:
				cur > 0 ? read_int(*(stack + cur - 1)) : write(STDOUT_FILENO, "-1\n", 3);
		}
	}
	return (0);
}


void	read_int(int v)
{
	char temp[7];
	int	size;

	size = itoa(temp, v);
	temp[size] = '\n';
	write(STDOUT_FILENO, temp, size + 1);
}

int itoa(char *dest, int n)
{
	int	div;
	int i;
   
	i = 0;
	div = 100000;
	while (!(n / div))
		div /= 10;
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

	while (read(STDIN_FILENO, &key, 1) && isdigit(key)) {
		ret *= 10;
		ret += key - '0';
	}
	return ret;
}

int	get_cmd(void)
{
	char	buf[3];
	char	key;

	read(STDIN_FILENO, buf, 3);
	while (read(STDIN_FILENO, &key, 1) && isalpha(key));

	if (buf[0] == 'p')
		return ((buf[1] == 'u') ? push : pop);

	if (buf[0] == 's')
		return (size);

	return ((buf[0] == 'e') ? empty : top);
}
