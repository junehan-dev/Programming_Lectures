#include <stdio.h>

int	find_min(int *nums, int n)
{
	int	l = 0;
	int	h = n - 1;
	int	m = h / 2;

	while (l < h) {
		if (nums[m] < nums[h]) {
			h = m;
		} else {
			l = m + 1;
		}
		m = (h + l) / 2;
	}
	return (m);
}

int	search(int *nums, int n, int t)
{
	int l;
	int h;
	int	mid;

	l = find_min(nums, n);
	if (nums[0] < nums[n - 1]) {
		l = 0;
		h = n - 1;
	} else if (t >= nums[0] && t <= nums[l - 1]) {

		l = 0;
		h = l - 1;
	} else if (t >= nums[l] && t <= nums[n - 1]) {
		l = l;
		h = n - 1;
	} else {
		return (-1);
	}

	mid = (l + h) / 2;
	while (l < h) {
		if (t > nums[mid]) {
			l = mid + 1;
		} else if (t < nums[mid]) {
			h = mid - 1;
		} else {
			return (mid);
		}
		mid = (l + h) / 2;
	}
	printf("mid : %d, l : %d, h : %d\n", mid, l, h);
	return (nums[mid] == t ? mid : -1);
}

int main(void)
{
	int test[] = {2};
	int ret = search(test,1, 2);

	printf("%d", ret);
	return (0);
}

