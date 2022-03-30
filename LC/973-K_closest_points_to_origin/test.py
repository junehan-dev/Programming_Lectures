from lib_minheap import build, insert, del_min

d = [];

ret = build(d);
insert(ret, 4);
insert(ret, 2);
insert(ret, 1);
insert(ret, 1);
print(ret);

min_out = del_min(ret);
print(min_out);
print(ret);

min_out = del_min(ret);
print(min_out);
print(ret);

min_out = del_min(ret);
print(min_out);
print(ret);

min_out = del_min(ret);
print(min_out);
print(ret);

min_out = del_min(ret);
print(min_out);
print(ret);

