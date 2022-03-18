grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


def count_island():
    counter: int; #ISLANDS
    linked_pair = []; #an Island linked to counted one
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == '0':
                print(m, n);
count_island();
print(grid);
