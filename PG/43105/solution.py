def solution(triangle):
    prev_row, *triangle = triangle;
    for row in triangle:
        max_summation(prev_row, row);
        prev_row = row;
    answer = max(triangle[-1])
    return answer

def max_summation(row, next_row):
    new_row = [None] * len(next_row);
    for i, v in enumerate(row):
        new_row[i] = (row[i] + next_row[i]) if new_row[i] is None else max([new_row[i], row[i] + next_row[i]]);
        new_row[i+1] = (row[i] + next_row[i+1]) if new_row[i+1] is None else max([new_row[i], row[i] + next_row[i+1]]);
    for i, v in enumerate(new_row):
        next_row[i] = new_row[i];


