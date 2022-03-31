import re
def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def cmp(c1, c2):
    c1_h, c1_n, c1_t = c1;
    c2_h, c2_n, c2_t = c2;

    if c1_h.lower() > c2_h.lower():
        return 1;
    elif c1_h.lower() < c2_h.lower():
        return -1;
    else:
        return int(c1_n) - int(c2_n);

def parse_header(s):
    header, *_  = re.split(r'[0-9]', s);
    left = s[len(header):]
    ed = 0;
    for i, ch in enumerate(left):
        if ch.isdigit():
            ed = i;
        else:
            break;
    number = left[:ed+1];
    tail = left[ed+1:];
    return (header, number, tail);


indata =  ["img12.png", "img012.png",  "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"];
new = [_ for _ in map(parse_header, indata)]
k = cmp_to_key(cmp)
out = sorted(new, key = k);
ret = ["".join(_) for _ in out];
print("CHECK-----------")
print(ret);
print(["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png", "img012.png" ]);
print("CHECK-----------")
print();



indata = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"];
new = [_ for _ in map(parse_header, indata)]
k = cmp_to_key(cmp)
out = sorted(new, key = k);
ret = ["".join(_) for _ in out];

print("CHECK-----------")
print(ret);
print(["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]);
print("CHECK-----------")
