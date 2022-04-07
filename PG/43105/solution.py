from functools import reduce

def solution(triangle):
    prev_row, *triangle = triangle;
    ret = reduce(max_summation, triangle, prev_row);
    return (max(ret));

def max_summation(row, next_row):
    new_row = [None] * len(next_row);
    for i, v in enumerate(row):
        new_row[i] = (
            (row[i] + next_row[i]) if
            new_row[i] is None else
            max([new_row[i], row[i] + next_row[i]])
        );

        new_row[i+1] = (
            (row[i] + next_row[i+1]) if
            new_row[i+1] is None else
            max([new_row[i], row[i] + next_row[i+1]])
        );

    return new_row;

ret = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

print(ret);
