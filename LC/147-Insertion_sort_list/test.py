from insertion_sort import insertion_sort, Node

head = Node(4);
prev = head;
ret = insertion_sort(head);
assert(ret is head);
assert(ret.next is None);


for v in range(4):
    node = Node(v);
    prev.next = node;
    prev = node;
for v in range(5,0, -1):
    node = Node(v);
    prev.next = node;
    prev = node;
ret = insertion_sort(head);


while(ret):
    print(ret.val);
    ret = ret.next;
