/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

#include <unistd.h>
#include <stdlib.h>

char	***groupAnagrams(char **strs, int strsSize,
						int *returnSize, int **returnColumnSizes)
{
	char ***ret;

	ret = malloc(sizeof(char ***));
	
	return (ret);
}
// {{"asc", "csa"}, {"abd"}} -> returnSize = 2
// {{"asc", "csa"}, {"abd"}} -> returnColsize = {2, 1};


int	main(void)
{
	int	strcnt = 6;
	char strs[7][4] = {"eat\0", "tea\0", "tan\0", "ate\0", "nat\0", "bat\0", 0};
	int set_count;
	int set_lens[6] = {0, 0, 0, 0, 0, 0};
	char ***ret;

	ret = groupAnagrams((char **)strs, strcnt, &set_count, (int**)set_lens);
	free(ret);

	return (0);
	
}
