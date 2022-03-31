import re

def qsort(array, left, right):
    if (right <= left):
        return ;
#    print("======START=======");

    lt_partition = left;
    cmp_index = lt_partition + 1;
    gt_partition = right;
    PIVOT = array[left];
#    print("PIVOT:", PIVOT);

    while (cmp_index <= gt_partition):
        is_bigger = cmp(array[cmp_index], PIVOT);
        if is_bigger < 0:
                swap(array, lt_partition, cmp_index);
                lt_partition += 1;
                cmp_index += 1;
        elif is_bigger > 0:
                swap(array, cmp_index, gt_partition);
                gt_partition -= 1;
        else:
            cmp_index += 1;


#    print("qsort left:[LEFT:lt+1]-",array[left:lt_partition]);
#    print("qsort fixed:[lt+1:gt+1]-", array[lt_partition:gt_partition +1]);
#    print("qsort right:[gt+1:RIGHT+1]-", array[gt_partition + 1:]);
#    print(array);
#    print("======FIN=======");
    
    qsort(array, left, lt_partition - 1);
    qsort(array, gt_partition + 1, right);

def swap(array, s1, s2):
    array[s1], array[s2] = array[s2], array[s1];

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
"""
indata =  ["img12.png", "img012.png",  "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"];
new = [_ for _ in map(parse_header, indata)]
qsort(new, 0, len(indata) - 1);
ret = ["".join(_) for _ in new];
print("CHECK-----------")
print(ret);
print(["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png", "img012.png" ]);
print("CHECK-----------")
print();



indata = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"];
new = [_ for _ in map(parse_header, indata)]
qsort(new, 0, len(indata) - 1);
ret = ["".join(_) for _ in new];

print("CHECK-----------")
print(ret);
print(["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]);
print("CHECK-----------")
"""

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
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

indata =  ["img12.png", "img012.png",  "kimg10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"];


new = [_ for _ in map(parse_header, indata)]
k = cmp_to_key(cmp)
print(sorted(new, key=k));
