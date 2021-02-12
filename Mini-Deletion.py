# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
We are given a string SS of length NN consisting only of letters A and/or B. Our goal is to obtain a string in the
format A...AB...B. (all letters A occur before all letters B) by deleting some letters from SS. In particular,
strings consisting only of letters A or only of letters B fit this format.
Write a function that, given a string SS, return the minimum number of letters that need to be deleted from SS in
order to obtain a string in the above format.
Example:
    Input: "BAAABAB"
    Output: 2
    Explanation: We can obtain "AAABB" by deleting the first occurrence of 'B' and the last occurrence of 'A'.
"""


def solution(S):
    min_deletions, left_b = 0, 0
    if not S:
        return min_deletions

    for k in S:
        if k == "A":
            min_deletions = min(left_b, min_deletions + 1)
        else:
            left_b += 1
    
    return min_deletions

    # A = [i for i in S if i != 'A']
    # B = [i for i in S if i != 'B']
    # A_B = len([i for i in B if i in B])

    # # length of items in S
    # N = len(S)

    # if A_B == 0:
    #     while N > 0 and N <= 100000:
    #         check = sorted(list(S))
    #         string = list(S)

    #         if string == check:
    #             # return True
    #             return len(check)
    #             break

    #         elif len(string) == 1:
    #             # return True
    #             return len(check)
    #             break
    #         else:
    #             # return False
    #             return 0
    #             break
    # else:
    #     return 0
