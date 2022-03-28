from antenna import placement

houses = [1,1,1,1,2];
count = 5;
expect = 1;
ret = placement(count, houses);

assert(ret == expect);

