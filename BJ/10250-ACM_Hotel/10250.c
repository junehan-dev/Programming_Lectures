#include <unistd.h>
#include <string.h>
#include <stdlib.h>

char    *itoa(int n);
int		get_num(void);
char	*get_roomnum(int n, int h);

int		main()
{
	int		len;
	int		i;
	int		h;
	int		n;
	char	**s;
	char	buf[6];

	len = get_num();
	s = (char **)malloc(sizeof(char *) * len);
	i = 0;
	while (i < len) {
		h = get_num();
		get_num();
		n = get_num();
		*(s + i) = get_roomnum(n, h);
		i++;
	}
	i = 0;	
	while (i < len - 1) {
		strcpy(buf, *(s + i));
		buf[strlen(*(s + i))] = '\n';
		buf[strlen(*(s + i)) + 1] = '\0';
		write(STDOUT_FILENO, buf, strlen(buf));
		free(*(s + i));
		i++;
	}

	strcpy(buf, *(s + i));
	buf[strlen(*(s + i))] = '\0';
	write(STDOUT_FILENO, buf, strlen(buf));
	free(*(s + i));
	free(s);
	return (0);
}

char	*get_roomnum(int n, int h)
{
	int		row;
	int		col;
	int		left;
	char	*ret;

	left = n % h;
	col = (left) ? left : h;
	row = n / h;
	row += (left) ? 1 : 0;

	ret = itoa(col * 100 + row);
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

