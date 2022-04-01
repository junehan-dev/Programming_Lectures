int	bin_search(int *nums, int n, int t)
{
	int l;
	int	m;

	if (n < 2)
		return (!n) ? -1 : ((*nums == t) ? 0 : -1);
	l = 0;
	m = (--n + l) / 2;
	while (l <= n) {
		if (!(*(nums + m) - t))
			return (m);
		*(nums + m) > t ? (n = m - 1) : (l = m + 1);
		m = (n + l) / 2;
	}
	return (-1);
	
}
#include <stdio.h>

int	main(void) {
	int	nums[] = {0,2,3,5};
	int	ret;
	int	t;

	
	t = 0;
	while (t < 10) {
		ret = bin_search(nums, 4, t);
		printf("%d  found at %d.\n",t, ret);
		t++;
	}
	return (0);
}
