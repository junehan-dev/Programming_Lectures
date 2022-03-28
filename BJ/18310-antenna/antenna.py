def placement(cnt, houses):
    qsort(houses, 0, cnt - 1);
    return houses[(cnt - 1) // 2];






def qsort(array, left, right):
    if (right <= left): # 칸이 하나 남았다면 종료
        return ;
    print("======START=======");

    lt_partition = left;
# |(시작)<--적은 파티션의 경계--|PIVOTS|<--큰 파티션 경계(종료)|
    cmp_index = lt_partition + 1; # 비교하는 인덱스의 주소
    gt_partition = right;     # PIVOT보다 큰값의 파티션을 나누는 i
    PIVOT = array[left]; # 매 호출마다 BOTTOM(0)번째
    print("PIVOT:", PIVOT);

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


    print("qsort left:[LEFT:lt+1]-",array[left:lt_partition]);
    print("qsort fixed:[lt+1:gt+1]-", array[lt_partition:gt_partition +1]);
    print("qsort right:[gt+1:RIGHT+1]-", array[gt_partition + 1:]);
    print(array);
    print("======FIN=======");
    
    qsort(array, left, lt_partition - 1);
    qsort(array, gt_partition + 1, right);

def swap(array, s1, s2):
    array[s1], array[s2] = array[s2], array[s1];

def cmp(c1, c2):
    if c1.isnumeric():#숫자비교
        return int(c1) - int(c2); 

    else:#문자열 비교
        if c1 > c2:
            return 1;
        elif c1 < c2:
            return -1;
        return 0;
