# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # Solution 1:
    # res = 1
    # A = list(set(A))
    # A.sort()
    # for i in A:
    #     if i == res:
    #         res += 1
    #     else:
    #         break
    # return res

    # Solution 2:
    res = 1
    A_set = set(A)
    for _ in range(len(A_set)):
        if res not in A_set:
            break
        res += 1
    return res
