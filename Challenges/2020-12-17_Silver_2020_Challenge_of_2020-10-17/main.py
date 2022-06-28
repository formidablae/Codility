def solution(A, B):
    sides = set(A).union(set(B))
    side_counts_dict = {el: 0 for el in sides}
    N_dim = len(A)
    for i in range(N_dim):
        if A[i] == B[i]:
            side_counts_dict[A[i]] = side_counts_dict[A[i]] + 1
        else:
            side_counts_dict[A[i]] = side_counts_dict[A[i]] + 1
            side_counts_dict[B[i]] = side_counts_dict[B[i]] + 1
    return max(side_counts_dict.values())


N = int(input())
A_array = list(map(int, input().split()))
B_array = list(map(int, input().split()))
print(solution(A_array, B_array))