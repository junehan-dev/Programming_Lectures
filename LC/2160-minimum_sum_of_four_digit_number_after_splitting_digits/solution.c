#include <stdio.h>

void swap(int *s1, int *s2);
int extract_min(int *num);

int	minimumSum(int num) {
	int min;
	int ret;
	
	ret = (extract_min(&num) + extract_min(&num)) * 10;
	ret += extract_min(&num);
	ret += extract_min(&num);

	return (ret);
}

int extract_min(int *num) {
	int min;
	int left;
	int cmp;
	int pos;

	left = 0;
	min = *num % 10;
	*num /= 10;
	pos = 1;
	while (*num) {
		cmp = *num % 10;
		*num /= 10;
		(min > cmp) ? swap(&min, &cmp): 0;
		left += cmp * pos;
		pos *= 10;
	}

	*num = left;
	return (min);
}

void swap(int *s1, int *s2) {
	int tmp;

	tmp = *s1;
	*s1 = *s2;
	*s2 = tmp;

	return;
}

int main(void) {
	int v;

	v = 8100;
	printf("%d", minimumSum(v));
	return (0);
}
