graph_data = [
    [0,1,1,1,0,0,0], #1
    [0,0,0,0,1,0,0], #2
    [0,0,0,0,1,0,0], #3
    [0,0,0,0,0,0,0], #4
    [0,0,0,0,0,1,1], #5
    [0,0,0,0,0,0,0], #6
    [0,0,1,0,0,0,0], #7
#   [1,2,3,4,5,6,7]
];

indexed_data = []
for row in graph_data:
    temp = [];
    for i, v in enumerate(row):
        if v:
            temp.append(i+1);
    indexed_data.append(temp);
print(indexed_data);

