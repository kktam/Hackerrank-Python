#!/bin/python3

import sys

def largestRectangle(h, N):
    stack = []
     
    max_area = 0
     
    idx = 0
    while (idx < N):
        if not stack or h[stack[-1]] <= h[idx]:
            stack.append(idx)
            idx += 1
        else:
             
            height_idx = stack.pop()
             
            depth = idx
            if stack:
                depth = idx - stack[-1] - 1
             
            area = h[height_idx] * depth
            max_area = max(area, max_area)
      
    while stack:
        height_idx = stack.pop()
             
        depth = idx
        if stack:
            depth = idx - stack[-1] - 1
             
        area = h[height_idx] * depth
        max_area = max(area, max_area)
             
    return max_area

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h, n)
    print(result)
