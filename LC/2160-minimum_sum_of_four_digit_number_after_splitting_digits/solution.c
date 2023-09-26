#include <stdio.h>

int extract_min(int *num);

int	minimumSum(int num) {
	int ret;
	int mul;

	mul = 1;
	ret = 0;
	while (num / 10) {
		mul = !mul;
		ret += extract_min(&num); 
		ret *= (mul) ? 10 : 1;
		num /= 10;
	}
	ret += num;
	return (ret);
}

int extract_min(int *num) {
	int tmp;
	int div;

	if (!(*num / 10))
		return (-1);

	div = 10;
	while (*num / div) {
		tmp = (*num / div) % 10;
		if ((*num % 10) > tmp) {
		 	*num -= tmp * div;
			*num += *num % 10 * div;
			*num -= *num % 10;
			*num += tmp;
		}
		div *= 10;
	}

	return (*num % 10);
}

int main(void) {
	int v;

	v = 1080344;
	printf("%d", minimumSum(v));
	return (0);
}
