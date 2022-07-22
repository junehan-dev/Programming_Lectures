#include <string.h>
#include <unistd.h>

bool isPalindrome(char *s)
{
	ssize_t end;
	ssize_t start;
	char s_alnum;
	char e_alnum;
	bool ret;

	ret = 1;
	start = 0;
	end = strlen(s) - 1;

	while (ret && start < end) {
		while (start < end && !((s_alnum = isalnum(*(s + start))) && (e_alnum = isalnum(*(s + end))))) {
			start = !s_alnum ? start + 1 : start;
			end = !e_alnum ? end - 1 : end;
		}
		
		ret = (start < end) ? (tolower(*(s + start++)) == tolower(*(s + end--))) : 1;
	}

	return (ret);
}
