#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#define MAX_BUF 13
#define MAX_STACK_SIZ 5000
enum CMDS	{ push = 1, pop, size, empty, top};

int		read_line(FILE *r_stream, char *dest);
int		itoa(char buf[], int n);
char	*get_num(char *buf);
int		get_cmd(char *buf);
void	read_int(int v, char end);
void	read_str(char *stack);
int		main()
{
	FILE *r_stream;
	char buf[MAX_BUF];
	char *stack[MAX_STACK_SIZ];
	int cur;
	int max;
	char end;

	r_stream = fdopen(0, "r");
	if (!r_stream)
		return (1);
	max = (read_line(r_stream, buf)) ? atoi(buf) : 0;
	cur = 0;
	end = '\n';
	while (max-- && read_line(r_stream, buf)) {
        switch (get_cmd((char *)buf)) {
			case push:
				*(stack + cur++) = get_num((char *)(buf + 5));
				break;
			case pop:
				if (cur > 0) {
					read_str(*(stack + --cur));
					free(*(stack + cur));
				} else {
					read_int(-1, end);
				}
				break;
			case size:
				cur ? read_int(cur, end): read_int(0, end);
				break;
			case empty:
				cur > 0 ? read_int(0, end) : read_int(1, end);
				break;
			default:
				cur > 0 ? read_str(*(stack + cur - 1)) :read_int(-1, end);
		}
	}
	while (cur--)
		free(*(stack + cur));

    fclose(r_stream);
	return (0);
}

void	read_str(char *stack)
{
	write(STDOUT_FILENO, stack, strlen(stack));
}
void	read_int(int v, char end)
{
	char temp[7];
	int	size;

	if (v > 0) {
		size = itoa(temp, v);
		temp[size++] = end;
	} else {
		size = (v == 0) ? 2 : 3;
		temp[0] = (v == 0) ? '0' : '-';
		temp[1] = (v == 0) ? end : '1';
		temp[2] = end;
	} 
	write(STDOUT_FILENO, temp, size);
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

char	*get_num(char *buf)
{
	return strdup(buf);
}

int	get_cmd(char *cmd)
{
	if (*(cmd + 0) == 'p')
		return ((*(cmd + 1) == 'u') ? push : pop);

	if (*(cmd + 0) == 's')
		return (size);

	return ((*(cmd + 0) == 'e') ? empty : top);
}

int read_line(FILE *r_stream, char *dest)
{
	return (dest == fgets(dest, MAX_BUF, r_stream)) ? 1 : 0;
}

