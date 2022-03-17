def solution(bridge_length, weight, truck_weights):
    bridge_q = [0] * bridge_length;
    answer = 0;
    bridge_data = [0, bridge_q];
    while(truck_weights or bridge_data[0] > 0):
        t = truck_weights[0] if truck_weights else 0;
        if (t == add_truck(bridge_data, weight, t)):
           truck_weights = truck_weights[1:]
        answer += 1;
        print(bridge_data);
    
    print(answer);
    return answer

def add_truck(b_data, max_w, to_add = 0):
    cur_w = b_data[0];
    out_w, *b_q = b_data[1];
    cur_w -= out_w;
    if not (cur_w + to_add < max_w + 1):
        to_add = 0;
    cur_w += to_add;
    b_data[0] = cur_w;
    b_q.append(to_add);
    b_data[1] = b_q;
    return to_add;

if __name__ == "__main__":
    bl, w, trs = [2, 10, [7,4,5,6]];
    print(bl, w, trs);
    ret = solution(bl, w, trs);
    assert(ret == 8);
    bl, w, trs = [100, 100, [10]];

    ret = solution(bl, w, trs);
    assert(ret == 101);
    bl, w, trs = [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]];
    ret = solution(bl, w, trs);
    assert(ret == 110);
    bl, w, trs = [100, 100, [10]];
    ret = solution(bl, w, trs);
    assert(ret == 101);

