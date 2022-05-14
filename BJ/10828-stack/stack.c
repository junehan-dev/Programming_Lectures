#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#define MAX_BUF 13
#define MAX_STACK_SIZ 5000
enum CMDS	{ push = 1, pop, size, empty, top};

char	*get_num(char *buf);
int		get_cmd(char *buf);
ssize_t	read_line(char *dest);
ssize_t	write_s(char *v);
ssize_t	write_int(int v);
int		itoa(char buf[], int n);
int		main(void)
{
	char buf[MAX_BUF];
	char *stack[MAX_STACK_SIZ];
	int cur;
	int max;

	max = (read_line(buf)) ? atoi(buf) : 0;
	cur = 0;
	while (max-- && read_line(buf) > 0) {
		switch (get_cmd((char *)buf)) {
			case push:
				*(stack + cur++) = strdup((const char *)(buf + 5));
				break;
			case pop:
				(cur && write_s(*(stack + --cur))) ? free(*(stack + cur)) : write(STDOUT_FILENO, "-1\n", 3);
				break;
			case size:
				(cur) ? write_int(cur) : write(STDOUT_FILENO, "0\n", 2);
				break;
			case empty:
				(cur) ? write(STDOUT_FILENO, "0\n", 2) : write(STDOUT_FILENO, "1\n", 2);
				break;
			default:
				(cur) ? write_s(*(stack + cur - 1)) : write(STDOUT_FILENO, "-1\n", 3);
		}
	}
	while (cur)
		free(*(stack + --cur));

	return (0);
}

ssize_t	write_int(int v)
{
	char	temp[7];
	size_t	len;

	len = itoa(temp, v);
	temp[len] = '\n';
	return write(1, temp, len + 1);
}

ssize_t	write_s(char *v)
{
	char	temp[7];
	size_t	len;

	len = strlen(v);
	memmove(temp, v, len);
	return write(STDOUT_FILENO, temp, len);
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

int	get_cmd(char *cmd)
{
	if (*(cmd + 0) == 'p')
		return ((*(cmd + 1) == 'u') ? push : pop);

	if (*(cmd + 0) == 's')
		return (size);

	return ((*(cmd + 0) == 'e') ? empty : top);
}

ssize_t read_line(char *dest)
{
	ssize_t ret;
	
	ret = read(STDIN_FILENO, dest, MAX_BUF);
	*(dest + ret) = '\0';
	return (ret);
}

