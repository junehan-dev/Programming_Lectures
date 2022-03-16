/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct FreqCounter {
	int value;
	unsigned int counter;
};

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize){
	int	i;
	int base_num;
	int	current_num;
	int	counter;
	FreqCounter mosts[k];
	
	i = 0;
	base_num = 1;
	counter = 0;

	// IF SORTED NUMS
	while (i < numsSize) {
		current_num = *(nums + i);
		if (base_num != current_num) {
			store(base_num, counter);
			base_num = current_num;
			counter = 0;
		}
		counter++;
		i++;
	}
	
}

store
