from antenna import placement
from sys import stdin

cnt = int(input());
houses = [_ for _ in map(int, stdin.readline().split(' '))];
print("cnt", cnt);
print("houses",houses);
ret = placement(cnt, houses);
print(ret);

