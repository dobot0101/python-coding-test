def solution(citations):
    citations.sort()
    l = len(citations)
    h_indexes = []
    for citation in citations:
        list = [i for i in citations if i >= citation]
        print(list, citation, l - len(list))
        if len(list) >= citation and (l - len(list)) <= citation:
            h_indexes.append(citation)
        print(h_indexes)
    return max(h_indexes)


print(solution([3, 0, 6, 1, 5]))