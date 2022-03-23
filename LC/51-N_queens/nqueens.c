/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

char *** solveNQueens(int n, int* returnSize, int** returnColumnSizes);
char	*ft_strcmp(char *s);
char	*create_board(int n);
char	**copy_board(char **board, int n);
void	free_board(char **board, int len);
int		check_board(char **board, int row, int col, int n);
int		dfs_start(char **board, int row, int n);

char ***dfs_start(char **board, int row, int n) {
    int col = 0;
    int counter = 0;
	char **new_board;
	char ***ret;
	
	if (row == n) {
		return board;
	}
	
	while (col < n)  {
		if check_board(new_board, row, col, n) {
			new_board = copy_board(board);
			*(ret + counter++) = new_board[row][col] = 'Q';
			dfs_start(new_board, row+1, n)
			counter++;
		}
		col++;
	}
	free_board(board);
	return (ret);
}

int check_plate(char **board, int row, int i, int n) {
    int j = 0;
    while (j < row) {
        if (board[j][i] == 'Q')
            return 0;
        if ((row - i < 0) && (*(*(board + j) + (row - i)) == 'Q'))
            return 0;
        if ((row + i < n) && (*(*(board + j) + (row + i)) == 'Q'))
            return 0;
        j++;
    }
    return 1;
}

void free_board(char **board, int n) {
    int i = 0;
    
    while (i < n)
        free(*(board + i++));
    free(board);
}

char	*ft_strcmp(char *s) {
	int		i;
	char 	*ret;
	i = 0;
	while (*(s + i))
		i++;
	ret = (char *)malloc(sizeof(char) * i);
	*(ret + i) = 0;

	while (i--) {
		*(ret + i) = *(s - i);
	}
	return (ret);
}

char **create_board(int n) {
	char	**ret;
	int		i;
	char 	*row;

	ret = (char **)malloc(sizeof(char *) * n);
	row = (char *)malloc(sizeof(char) * n + 1);

	i = 0;
	while (i < n)
		*(row + i++) = '.';

	*(row + i) = 0;
	*ret = row;
	i = 1;
	while (i < n)
		*(ret + i++) = ft_strcmp(row);

	return (ret);
}


char **copy_board(char **board, int n) {
	char **ret;
	int row, col;

	ret = create_board(n);

	row = 0;
	while (row < n) {
		col = 0;
		while (col < n) {
			ret[row][col] = board[row][col];
			col++;
		}
		row++;
	}

	return (ret);
}

int	check_board(char **board, int row, int col, int n)
{
	int cmp_row;
	int cmp_col;

	cmp_row = 0;
	while (cmp_row < row) {
		if (board[cmp_row][col] == 'Q')
			return (0);
		if ((col - cmp_row) > 0 && board[cmp_row][col - cmp_row] == 'Q')
			return (0);
		if ((col + cmp_row) < n && board[cmp_row][col + cmp_row] == 'Q')
			return (0);
	}

	return (1);
}


char *** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    char ***ret;

    ret = dfs_start(, 0, n);
    printf("%d in chess plate\n", ret);

    return ret;
}

