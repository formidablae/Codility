# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    res = 0
    depths = {}
    wall = A[0]
    for i in range(1, len(A)-1):
        if A[i] > wall:
            wall = A[i]
        else:
            depths[i] = wall - A[i]
    
    wall = A[len(A)-1]
    for i in range(len(A)-2, 0, -1):
        if A[i] > wall:
            wall = A[i]
        elif i in depths.keys():
            res = max(res, min(wall - A[i], depths[i]))
    return res


if __name__ == "__main__":
    A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
    print(solution(A))
