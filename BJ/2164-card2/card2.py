def get_input():
    return (int(input()));

def card2(n):
    queue = [_ for _ in range(1, n + 1)];
    
    while (len(queue) > 1):
        if (len(queue) % 2):
            queue = queue[-1:] + [v for i, v in enumerate(queue) if i % 2];
        else:
            queue = [v for i, v in enumerate(queue) if i % 2];
    return (queue[0]);


if __name__ == "__main__":
    print(card2(get_input()));
