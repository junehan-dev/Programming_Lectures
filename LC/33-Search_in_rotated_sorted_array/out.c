#include <stdio.h>
int	find_min(int *nums, int n)
{
	int	l = 0;
	int	m = n / 2;
	int	h = n - 1;

	if (nums[0] < nums[n-1])
		return (0);

	while (l <= h) {
		if (nums[m] < nums[l]) {
			h = m;
			l += 1;
		} else if (nums[m] > nums[h]) {
			l = m + 1;
		} else {
			return (m);
		}

		m = (h + l) / 2;
	}

	return (m);
}

int	search(int *nums, int n, int t)
{
	int min;

	if (t > n-1)
		return (-1);

	min = find_min(nums, n);
	return (((min + t) > (n - 1)) ? nums[min + t - n] : nums[min + t]);
}

