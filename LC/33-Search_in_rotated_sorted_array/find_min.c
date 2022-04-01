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
