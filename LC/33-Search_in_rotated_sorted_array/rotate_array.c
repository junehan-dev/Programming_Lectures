#include <unistd.h>
void	swap(void *s1, void *s2, size_t siz);
void	rotate(int	*nums, int t, int n)
{
	int	i;

	i = 0;
	while (t < n) {
		swap(nums + i++, nums + t++, sizeof(t));
	}
}

void	swap(void *s1, void *s2, size_t siz)
{
	size_t	rb;
	char	tmp[siz];
	char	*s1_pt;
	char	*s2_pt;

	rb = 0;
	s1_pt = (char *)s1;
	s2_pt = (char *)s2;
	while (rb < siz) {
		tmp[rb++] = *s1_pt;
		*s1_pt++ = *s2_pt++;
	}
	while (rb > 0)
		*(--s2_pt) = tmp[--rb];
}


#include <stdio.h>
int	main(void)
{
	int	test[9] = {0,3,4,5,6,8,9,10,22};
	rotate(test, 5, 9);
	int i;
	i = 0;
	while (i++ < 9)
		printf("%d ", test[i-1]);
}
