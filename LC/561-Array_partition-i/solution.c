#include <stdio.h>
void stat(int *nums, int start, int end);
void qsort(int *nums, int start, int end);
void swap(int *nums, int s1, int s2);
int	arrayPairSum(int *nums, int numSize)
{
	int ret;
	int i;

	ret = 0;
	qsort(nums, 0, numSize - 1); 
	
	i = 0;
	while (i < numSize) {
		ret += (*(nums + i));
		i += 2;
	}
	return (ret);
}

void qsort(int *nums, int start, int end)
{
	int	left_end;
	int	right_start;

	stat(nums, start, end);
	if ((end - start) < 1)
		return ;

	left_end = start + 1;
	right_start = end;
	swap(nums, start, (start + end) / 2);
	printf("mid : %d left_end: %d right_start: %d\n", *(nums + start), left_end, right_start);
	while (left_end < right_start)
		(*(nums + start) < *(nums + left_end)) ? swap(nums, left_end, right_start--) : left_end++;

	if (*(nums + start) > *(nums + left_end)) {
		swap(nums, start, left_end);
	} else {
		swap(nums, start, --left_end);
		right_start--;
	}
	printf("SORTED: nums[%d]: %d\n", left_end, *(nums + left_end));
	qsort(nums, start, left_end - 1);
	qsort(nums, right_start + 1, end);

	return ;
}

void swap(int *nums, int s1, int s2)
{
	int temp;

	temp = *(nums + s1);
	*(nums + s1) = *(nums + s2);
	*(nums + s2) = temp;
	return ;
}


void stat(int *nums, int start, int end) {
	while (start <= end) {
		printf("nums[%d]: %d ", start, *(nums+start));
		start++;
	}
	printf("\n");	
}
int main(void) {
	int nums[] = {2, 4, 5, 1,6, 4, 3, 5};
	int i;

	i = 0;
	
	qsort((int *)nums, 0, 7);
	stat(nums, 0, 7);

	return 0;
}
