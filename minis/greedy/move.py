def command(cmds, n):
    x, y = [0, 0];

    for key in cmds:
        if key == "R" and x < n - 1:
            x += 1;
        elif key == "L" and x > 0:
            x -= 1;
        elif key == "U" and y > 0:
            y -= 1;
        elif key == "D" and y < n - 1:
            y += 1;
    return (x, y);

def run():
    end = command(["R", "R", "R", "U", "D", "D"], 5);
    print(end);

run();
