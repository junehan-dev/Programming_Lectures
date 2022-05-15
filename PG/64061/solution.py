def solution(board, moves):
    answer = 0
    stack = [];
    for move in moves:
        poped = stack_pop(board, move);
        if poped:
            stack_store(stack, poped);
            answer += stack_post(stack);
    return answer * 2;

def stack_pop(board, move):
    poped = None;
    move -= 1;
    for i in range(len(board)):
        if board[i][move]:
            poped, board[i][move] = board[i][move], 0;
            break;
    return poped;

def stack_store(stack, poped):
    stack.append(poped);

def stack_post(stack):
    if (len(stack) > 1 and stack[-1] == stack[-2]):
        stack.pop();
        stack.pop();
        return (1);
    return (0);

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
    moves = [1,5,3,5,1,2,1,4];
    assert(solution(board, moves) == 2 * 2);

