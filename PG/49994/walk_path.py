def walk(cmds, log):
    if not cmds:
        return log;
    cmd_map = 'UDLR';
    x = [0, 0, -1, 1];
    y = [1, -1, 0, 0];
    cur = [0, 0]; 
    for key in cmds:
        i = cmd_map.index(key);
        cmd = (x[i], y[i]);
        register(log, cur, cmd);

    return log;

def register(log, cur, cmd):
    from_x, from_y = cur;
    to_x = from_x + cmd[0];
    to_y = from_y + cmd[1];
    
    if not ((to_x > 5 or to_x < -5) or (to_y > 5 or to_y < -5)):
        print(cur, "->", (to_x,to_y));
        reverse = log.get(f"{to_x}{to_y}", None);
        if not reverse or f"{from_x}{from_y}" not in reverse:
            if f"{from_x}{from_y}" in log:
                log[f"{from_x}{from_y}"].add(f"{to_x}{to_y}");
            else:
                log[f"{from_x}{from_y}"] = {f"{to_x}{to_y}"};
        cur[0] = to_x;
        cur[1] = to_y;
        

def solution(dirs):
    log = {};
    walk(dirs, log);
    answer = 0;
    for key in log:
        answer += len(log[key]);
    return answer

