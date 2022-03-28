from antenna import placement
from sys import stdin

cnt = int(input());
"""
houses = [_ for _ in map(int, stdin.readline().split(' '))];
print("cnt", cnt);
print("houses", houses);
ret = placement(cnt, houses);
print("houses", houses);
print(ret);
"""

chars = [v for v in stdin.readline().split(' ')];
chars[-1] = chars[-1][0];
ret = placement(cnt,chars);
