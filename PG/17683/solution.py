def solution(m, musicinfos):
    ret = None;
    max_playtime = 0;
    m = replace_sharp(m);
    while ret is None and len(musicinfos):
        info = musicinfos.pop();
        playtime = get_playtime(info);
        if playtime >= len(m):
            *_, name, lyric = info.split(",");
            lyric = replace_sharp(lyric);
            if playtime == len(m) and lyric == m:
                if playtime > max_playtime:
                    ret = name;
                    max_playtime = playtime;
            elif playtime > len(m):
                played = get_playback(lyric, playtime);
                if m in played:
                    if playtime > max_playtime:
                        ret = name;
                        max_playtime = playtime;
    return ret if ret is not None else "(None)";
    
def get_playback(lyric, playtime):
    if len(lyric) > playtime:
        return lyric[:playtime];
    elif len(lyric) == playtime:
        return lyric;
    else:
        played = playtime // len(lyric);
        ended = playtime % len(lyric);
        return lyric * played + lyric[:ended] if ended else lyric * played;

def replace_sharp(lyric):
    lyric = lyric.replace("#C", "1");
    lyric = lyric.replace("#D", "2");
    lyric = lyric.replace("#F", "3");
    lyric = lyric.replace("#G", "4");
    lyric = lyric.replace("#A", "5");
    return lyric

def get_playtime(musicinfo):
    start, end, *_ = musicinfo.split(",");
    mins, secs = end.split(":");
    playtime = (int(mins) * 60 + int(secs));
    mins, secs = start.split(":");
    playtime -= (int(mins) * 60 + int(secs));
    return playtime;


if __name__ == "__main__":
    INPUTS = [
        ["ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], "HELLO"],
        ["CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], "FOO"],
        ["ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"], "WORLD"]
    ]
    for INPUT in INPUTS:
        print(solution(INPUT[0], INPUT[1]));
