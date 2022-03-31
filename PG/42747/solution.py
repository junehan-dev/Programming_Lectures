def solution(citations):
    citations.sort(reverse=True);
    for i in range(len(citations)):
        if citations[i] <= i + 1:
            return citations[i];
    return (citations[i]);
    
print(solution([10,8]))
#print(solution([1,0,6,5,5,5,0]));
