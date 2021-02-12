# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# https://assets.leetcode.com/users/images/d5f62610-dae7-4ec0-9ad0-ec70a1e9c25a_1596946491.193315.png

def checkMAx(blocks, i, n):
    left = i 
    right = i

    right_most = False
    left_most = False

    while left >= 0 and right < n and (not right_most or not left_most):
        if right + 1 < n and blocks[right] <= blocks[right + 1]:
            right += 1
        else:
            right_most = True

        if left - 1 >= 0 and blocks[left] <= blocks[left - 1]:
            left -= 1
        else:
            left_most = True
    
    return right - left + 1

def solution(blocks):
    n = len(blocks)
    
    max_value = 1
    for i in range(n):
       temp = checkMAx(blocks, i, n)
       max_value = max(max_value, temp)
    
    return max_value
