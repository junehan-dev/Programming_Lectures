def command(cmds, n):
    x, y = [0, 0];

    for key in cmds:
        if key == "R":
            x = x+1 if x < n - 1 else x
        elif key == "L":
            x -= 1 if x > 0 else x;
        elif key == "U":
            y -= 1 if y > 0 else y;
        else:
            y += 1 if y < n - 1 else y;
    return (x, y);

def run():
    end = command(["R", "R", "R", "U", "D", "D"], 5);
    print(end);

run();

def book(cmds):
    x, y = 1, 1;
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0];

    move_types = ["L", "R", "U", "D"];
    for cmd in cmds:
        for i in range(move_types):
            if plan == move_types[i]:
                nx = x + dx[i];
                ny = y + dy[i];
        
