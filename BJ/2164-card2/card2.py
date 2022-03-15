def get_input():
    return (int(input()));

def card2(n):
    queue = [_ for _ in range(1, n + 1)];

    if not queue:
        return None;

    while (queue):
        ret, queue = dequeue(queue);
        if not (queue):
            return ret;

        deq_data, queue = dequeue(queue);
        queue = enqueue(queue, deq_data);

def enqueue(queue, data):
    return (queue + [data]);
    
def dequeue(queue):
    data, *queue = queue;
    return (data, queue);

if __name__ == "__main__":
    print(card2(get_input()));
