/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void pseudo(void)
{
	char *strs[] = {"eat", "tea", "tan", "ate", "nat", "bat"};
	int i = 0;
	int	len;
	char	*base;
	char	*cmp;
	char	*temp[];

	while (*strs && *(strs + 1)) {
		if (**strs) {
			base = *strs;
			cmp = *(strs + 1);
			while (cmp) {
				if (is_anagram(base, cmp++)) {
					store(temp, cmp - 1); // 빼고
					cmp - 1 = "";// 빈문자임을 표시
				}
			}
			store(temp, base); // Base 빼고 빈문자
			base = "";
		}
		store(big_temp, temp); // temp에 모은걸 밖으로 이동하고,
		temp = []; // temp 비우기
	}
	return (big_temp);
}


int	is_anagram(const char *s1, const char *s2)
{
	char	temp[128] = {0};
	int		i;
	
	while (*s1 && *s2) {
		temp[(s1++ - 'a')]++;
		temp[(s2++ - 'a')]--;
	}

	if (!*s1 || !*s1)
		return (0);

	while (i < 128)	
		if (temp[i++])
			return (0);
	return (1);
}


