#include <string.h>
#include <assert.h>
#include <unistd.h>
#define MAX_CHARS 26

int	find_alpha(const char *s);
int hh_strchr(const char *s, char ch);
size_t print_with_delimiter(int s[], char del);

int	main(int argc, const char *argv[])
{
	assert(argc == 2);
	assert(strlen(argv[1]) < 101);
	return (find_alpha(argv[1]));
}

int	find_alpha(const char *s)
{
	int ch;
	int pos_arr[MAX_CHARS];
	int i;

	ch = 'a';
	i = 0;
	while ((ch + i) < ('z' + 1))
		pos_arr[i++] = hh_strchr(s, ch + i);

	print_with_delimiter(pos_arr, ' ');
	return (0);
}

int hh_strchr(const char *s, char ch)
{
	int i;

	i = 0;
	while (*(s + i) != ch && *(s + i))
		i++;

	return (!*(s + i) ?  -1 : i);
}

size_t print_with_delimiter(int pos[], char del)
{
	int	i;
	char temp[MAX_CHARS * 3];
	size_t len;

	i = 0;
	len = 0;
	while (i < MAX_CHARS) {
		if (pos[i] == -1) {
			temp[len++] = '-';
			temp[len++] = '1';
		} else if (pos[i] > 9) {
			temp[len++] = pos[i] / 10 + '0';
			temp[len++] = pos[i] % 10 + '0';
		} else {
			temp[len++] = pos[i] + '0';
		}
		temp[len++] = del;
		i++;
	}

	temp[--len] = '\0';
	assert(len == write(1, temp, len));
	return (len);
}
