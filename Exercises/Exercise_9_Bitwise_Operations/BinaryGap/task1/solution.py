"""
A binary gap within a positive integer N is any maximal sequence of
consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and
contains a binary gap of length 2.
The number 529 has binary representation 1000010001
and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and
contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5,
because N has binary representation 10000010001 and
so its longest binary gap is of length 5.
Given N = 32 the function should return 0,
because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
    - N is an integer within the range [1..2,147,483,647].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    """
    :param N: int
    :return: int
    """
    # write your code in Python 3.6
    binary_str = bin(N)[2:]
    
    sequences = []
    
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            if len(sequences) == 0:
                sequences.append({"start": i, "end": None})
            elif sequences[-1]["start"] == i - 1:
                sequences[-1]["start"] = i
            elif sequences[-1]["end"] is None:
                sequences[-1]["end"] = i
                sequences.append({"start": i, "end": None})
            else:
                sequences.append({"start": i, "end": None})
    valid_sequences = [seq for seq in sequences if seq["end"] is not None]
    if len(valid_sequences) == 0:
        return 0
    longest_sequence = max(valid_sequences, key=lambda x: x["end"] - x["start"])
    return longest_sequence["end"] - longest_sequence["start"] - 1


N_s = [1041, 32, 15, 529, 9, 20, 10, 0, 1, 3, 5]

for N in N_s:
    print(f"N = {N}, binary N = {bin(N)[2:]}, longest binary gap = {solution(N)}")
