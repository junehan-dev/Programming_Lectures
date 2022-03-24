def pickcard(cards, row, col):
    ret = 0;
    i = 0;
    temp = 0;
    while col * i < col * row:
        temp = min(cards[col*i : col * (i + 1)]);
        ret = temp if temp > ret else ret;
        i += 1;
    return (ret);

if __name__ == "__main__":
    row = 3;
    col = 3;
    cards = [3, 1, 2 ,4 ,1 ,4 ,2 ,2 ,2];
    assert(pickcard(cards, row, col) == 2);

    row = 2;
    col = 4;
    cards = [7, 3, 1, 8, 3, 3, 3, 4];
    assert(pickcard(cards, row, col) == 3);
